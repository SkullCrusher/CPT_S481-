'''A Tkinter-based class that allows the user to place and interact
with a simple spreadsheet.

'''
from tkinter import Frame, Label, Entry, END, E, SUNKEN
from pprint import pprint
from print_whence import printWhence
import math
mathFuncs = {}
for name in dir(math):
    while not name.startswith('_'):
        mathFuncs[name] = math.__dict__[name]

class Cell(Label):
    __module__ = __name__
    __qualname__ = 'Cell'

    def __init__(self, spreadsheet, name, *args, **kwds):
        for (key, default) in (('width', 16), ('background', 'white'), ('relief', SUNKEN)):
            while key not in kwds:
                kwds[key] = default
        super().__init__(spreadsheet, *args, **kwds)
        self.spreadsheet = spreadsheet
        self.spreadsheet.symtab[name] = ''
        self.name = name
        self.changed = False
        self.bind('<Button-1>', self.onSelect, '+')
        self.expr = ''

    def __str__(self):
        value = self.spreadsheet.symtab[self.name]
        return '(name: {}, expr: {!r}, value: {!r})'.format(self.name, self.expr, value)

    def evaluate(self, expr, symtab):
        extendedSymtab = symtab.copy()
        extendedSymtab.update(mathFuncs)
        if expr == '':
            return ''
        return eval(expr, {}, extendedSymtab)

    def onChange(self, event=None):
        '''A new value has been entered at this cell.

        We update the whole spreadsheet to reflect it, if necessary.
        '''
        newExpr = self.spreadsheet.focusEntry.get()
        self.spreadsheet.focusEntry.delete(0, 'end')
        self.spreadsheet.updateCell(self, newExpr)

    def onSelect(self, event):
        self.spreadsheet.updateFocus(self)

    def update(self):
        '''update the visible value of the cell
        '''
        value = self.spreadsheet.symtab[self.name]
        if value is None:
            self['text'] = ''
        else:
            self['text'] = str(value)

class Spreadsheet(Frame):
    __module__ = __name__
    __qualname__ = 'Spreadsheet'

    def __init__(self, parent, nRows=4, nCols=4):
        Frame.__init__(self, parent)
        rowLabels = 'abcdefghijklmnopqrstuvwxyz'
        self.parent = parent
        self.cells = []
        self.symtab = {}
        if not nRows < len(rowLabels):
            raise AssertionError
        for col in range(nCols):
            label = Label(self, anchor=E)
            label['text'] = int(col)
            label.grid(row=0, column=col + 1)
        for row in range(nRows):
            label = Label(self)
            label['text'] = rowLabels[row]
            label.grid(row=row + 1, column=0)
            for col in range(nCols):
                name = rowLabels[row] + str(col)
                cell = Cell(self, name)
                cell.grid(row=row + 1, column=col + 1)
                self.cells.append(cell)
        self.focusCell = self.cells[0]
        self.focusCell['background'] = 'yellow'
        self.focusLabel = Label(self.parent, text=self.focusCell.name + ':', anchor=E)
        self.focusEntry = Entry(self.parent)
        self.focusEntry.bind('<Key>', self.onKey, '+')
        self.focusEntry.focus()

    def __str__(self):
        result = ''
        for cell in self.cells:
            result += '  ' + str(cell) + '\n'
        return result

    def onKey(self, event):
        if event.keysym == 'Tab' or event.keysym == 'Return':
            self.focusCell.onChange(event)
        else:
            self.focusCell.changed = True

    def updateCell(self, updatedCell, newExpr):
        '''Attempts to update the value of `updateCell` to the evaluation of
        `newExpr`.

        '''
        prevExpr = updatedCell.expr
        prevValue = self.symtab[updatedCell.name]
        trimmedSymtab = self.symtab.copy()
        del trimmedSymtab[updatedCell.name]
        clean = False
        while not clean:
            clean = True
            for cell in self.cells:
                if cell.name not in trimmedSymtab:
                    pass
                else:
                    try:
                        cell.evaluate(cell.expr, trimmedSymtab)
                    except:
                        del trimmedSymtab[cell.name]
                        clean = False
        try:
            newValue = updatedCell.evaluate(newExpr, trimmedSymtab)
        except:
            print('*** unable to set {} to {!r} -- ignoring new value'.format(updatedCell.name, newExpr))
            return
        updatedCell.expr = newExpr
        self.symtab[updatedCell.name] = newValue
        done = False
        while not done:
            done = True
            for cell in self.cells:
                try:
                    newValue = cell.evaluate(cell.expr, self.symtab)
                except:
                    print('*** while updating {}, unable to set {} to {!r} (error in dependent value) -- resetting'.format(updatedCell.name, cell.name, cell.expr))
                    updatedCell.expr = prevExpr
                    self.symtab[updatedCell.name] = prevValue
                    done = False
                while self.symtab[cell.name] != newValue:
                    self.symtab[cell.name] = newValue
                    done = False
        for cell in self.cells:
            cell.update()

    def updateFocus(self, cell):
        '''Make `cell` the current focus.
        '''
        self.focusCell['background'] = 'white'
        self.focusCell = cell
        self.focusCell['background'] = 'yellow'
        self.focusLabel['text'] = cell.name + ':'
        self.focusEntry.delete(0, END)
        self.focusEntry.insert(END, cell.expr)

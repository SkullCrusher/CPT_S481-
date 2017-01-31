from tkinter import *
import math

# Useful globals.
alphabet = "abcdefghijklmnopqrstuvwxyz"
cellWidth = 15 # How wide each excel cell is.
cell_background_default = "white"
cell_background_highlight = "yellow" # "gold" is better imo but pdf says "yellow".

"""
    The excel sheet is made out of cells. Each cell is clickable and holds both value and expression for it.
"""
class Cell(Label):

    """
        Handle user click, this could be done with a lambda function but this seems cleaner.
    """
    def cellclick(self, event):
        self.spreadsheet.switchcells(self)

    """
        Init, does the following:
            1. Overrides the arguments to set the background color, excel cell width, and the styling for cells.
            2. Calls the init for the inherited label class.
            3. Set values into the cell.
            4. Add a click listener to change the highlighted cell.
    """
    def __init__(self, spreadsheet, name, *args, **kwds):

            # Overwrite the arguments with the settings to make it look like the picture.
        kwds["background"] = cell_background_default
        kwds["width"] = cellWidth
        kwds["relief"] = GROOVE

            # Init parent.
        super().__init__(spreadsheet, *args, **kwds)

            # Set up the cell object.
        self.spreadsheet = spreadsheet

            # Create a dictionary to hold the custom namespace elements we pass to eval.
        self.spreadsheet.symbols[name] = ""

            # Store the name of the cell, aka a0, b2, etc.
        self.name = name

            # The value of the excel.
        self.value = ""

            # The expression that the cell contains, aka "4 + 4 * a0".
        self.expression = ""

            # Bind mouse click to trigger when they click on a excel cell.
        self.bind("<Button-1>", self.cellclick, "+")

    """
        Do the evaluation on the current cell.
    """
    def evaluate(self, expression, namespacesymbols):

            # Prevent evaluating the cell if it"s actually just empty.
        if expression == "" or expression is None:
            return ""

            # Eval the string provided with the namespaces.
        return eval(expression, {}, namespacesymbols)

    """
        Used to update the value of each excel cell based on the value stored in the sheet.
    """
    def update(self):
            # Get the value from the spreadsheet.
        self.value = self.spreadsheet.symbols[self.name]

            # If there is a not a set value, or it is empty set it to empty.
        if self.value is None or self.value is "":
            self["text"] = ""
        else:
            self["text"] = str(self.value)



"""
    Spreadsheet, this class is used to build a excel frame inside a window.

        The class inherits from the tkinter frame class and does the following:
            1. Generates a excel cell grid based on user input size.
            2. Handles user input to control the excel grid.
                2.1. Selecting a excel cell.
                2.2. Entering complex python expressions to set the values of the cells.

    Example usage:
        from tkinter import Tk

        from spreadsheet import Spreadsheet

        root = Tk()
        spreadsheet = Spreadsheet(root, 4, 4)
        spreadsheet.grid(row=0, column=0, columnspan=4)
        spreadsheet.focusLabel.grid(row=1, column=0)
        spreadsheet.focusEntry.grid(row=1, column=1)
        root.mainloop()
"""
class Spreadsheet( Frame ):

    """
        Create the column numbers at the top of the excel grid.
    """
    def _generateMenuLabel_Numbers(self):
        for i in range(self.nc):
            label = Label(self)
            label["text"] = i
            label.grid(row=0, column = (i + 1))

    """
        Create the row letters on the left side of the excel grid.
    """
    def _generateMenuLabel_Letters(self):
        for i in range(self.nr):
            label = Label(self, width = 3)

                # Alphabet is the alphabet in order so they map one to one with a for loop.
            label["text"] = alphabet[i]
            label.grid(row = (i + 1), column=0)

    """
        Create the excel cells, populate them, and place them into the cell's grid.
    """
    def _generateExcelLabels(self):
        for row in range(self.nr):
            for col in range(self.nc):
                    # Generate the name of the excel cell.
                name = alphabet[row] + str(col)

                    # Create a new excel cell.
                cell = Cell(self, name)

                    # Spawn the cell into the frame via grid.
                cell.grid(row = (row + 1), column = (col + 1))

                    # Put the new cell into the array of cells based on row and column.
                self.cells[col][row] = cell

    """
        Init, this does the following:
            1. Calls the init of the inherited frame class.
            2. Store constants into the spreadsheet.
            3. Bind the custom focusLabel and focusEntry so the caller can grid them.
            4. Set up key bind to listen on user input to see if they finished entering a new string.
    """
    def __init__(self, root, row, column):

            # init the parent frame.
        Frame.__init__(self, root)

            # Store the tkinter object thingy that called us.
        self.parent = root

            # Store the number of rows and columns.
        self.nr = row
        self.nc = column


            # Make a grid to store the cells inside the frame (that the user can interact with).
        self.cells = [[0 for x in range(column)] for y in range(row)]

            # Namespace didn"t seem like a appropriate name so I guess symbols will work
            # but this hold all the stuff passed to eval.
        self.symbols = {}

            # Add the entire math library to the list of namespace elements passed to eval.
        self.symbols.update(math.__dict__)


            # Generate the numbers above columns based on the input number of columns.
        self._generateMenuLabel_Numbers()

            # Generate the letters beside the columns based on the input number of rows.
        self._generateMenuLabel_Letters()

            # Generate the excel cells which site in the middle and the user can edit.
        self._generateExcelLabels()


            # Set pick a default cell to have highlighted, I am doing [0][0] because the pdf picture has it being default.
        self.currentcell = self.cells[0][0]
        self.currentcell["background"] = cell_background_highlight


            # put the entry so the parent can place the input box. I use a default of x:3, y:8 but the parent overrides it.
        self.focusEntry = Entry(self.parent)
        self.focusEntry.grid(column=3, row=8)

            # place in the label for the editing textbox.
        self.focusLabel = Label(self.parent,anchor=W)
        self.focusLabel["text"] = text=self.currentcell.name + ": "
        self.focusLabel.grid(row=12, column=0)

            # Add a hook to process the user input.
        self.focusEntry.bind("<Key>", self.userinput_callback, "+")

    """
        This is called when the user presses a key, if it is return or tab we eval all of the cells else do nothing.
    """
    def userinput_callback(self, event):
        if str(event.keysym).upper() == "RETURN" or str(event.keysym).upper() == "TAB":
            self.evalulatecells(self, self.focusEntry.get())

    """
        This is used to swap to a new highlighted excel cell.
    """
    def switchcells(self, arg):

            # Reset the color on the current cell.
        self.currentcell["background"] = cell_background_default

            # Swap to the new cell and set it's color to highlighted.
        self.currentcell = arg
        self.currentcell["background"] = cell_background_highlight

            # Change the label for the selected excel cell.
        self.focusLabel["text"] = arg.name + ": "


            # Clear out the current expression before putting the new one or else it duplicates
        self.focusEntry.delete(0, END)

            # Set the expression from the currently selected cell into the textbox
        self.focusEntry.insert(END, arg.expression)

    """
        This is the algorthm from the homework pdf, it's very confusing but it will prevent issues.
    """
    def evalulatecells(self, cell, newexpression):

        e_prime = self.currentcell.expression
        v_prime = self.symbols[self.currentcell.name]

            # {First, create a symbol table that makes no reference to p.}
        s = self.symbols.copy()
        del s[self.currentcell.name]
        clean = False
        while not clean:
            clean = True

            for x in range(self.nc):
                for y in range(self.nr):
                    cell = self.cells[x][y]

                    if cell.name in s:
                        try:
                            cell.evaluate(cell.expression, s)
                        except:
                            del s[cell.name]
                            clean = False

            # {Then, try to evaluate the new value for p with the prunded symbol table.}
        try:
            v = self.currentcell.evaluate(newexpression, s)
        except:
            print("Error with input.")
            return

            # {Then, (tentatively) update p's expression and value.}
        self.currentcell.expression = newexpression
        self.symbols[self.currentcell.name] = v

            # {Finally, either update all cells to reflect the new value of p or if there are any errors unto everything}
        okay = True
        done = False
        while not done:
            done = True
            for x in range(self.nc):
                for y in range(self.nr):
                    cell = self.cells[x][y]

                    try:
                        v = cell.evaluate(cell.expression, self.symbols) #{using the original symbol table}
                    except:
                        self.currentcell.expression= e_prime
                        self.symbols[self.currentcell.name] = v_prime
                        done = False
                        okay = False
                        print("Error with input.")

                    while self.symbols[cell.name] != v:
                        self.symbols[cell.name] = v
                        done = False # {keep propagating}

            # The user input is okay, update all of the cells.
        for x in range(self.nc):
            for y in range(self.nr):
                self.cells[x][y].update()

        return okay



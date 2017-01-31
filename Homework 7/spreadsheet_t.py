from tkinter import Tk

from spreadsheet import Spreadsheet

root = Tk()
spreadsheet = Spreadsheet(root, 4, 4)
spreadsheet.grid(row=0, column=0, columnspan=4)
spreadsheet.focusLabel.grid(row=1, column=0)
spreadsheet.focusEntry.grid(row=1, column=1)
root.mainloop()

from tkinter import *

class SheetSelection():
    '''
    Selects a sheet given multiple options
    '''

    def __init__(self, sheet_names, selected_sheet, root):
        '''
        (SheetSelection, list of str, StingVar, Tk)

        Mutates the selected sheet from user input
        '''
        # make a root
        self._root = root

        # Ask the user what they would like to pick
        my_label = "Which sheet are you going to be uploading?"
        label = Label(self._root, text=my_label)
        label.grid()

        # then what is wanted is to make a "dropdown" option list
        menu = OptionMenu(self._root, selected_sheet, *sheet_names)
        menu.grid()

        # create a select button; once the user presses select, the string
        # gets returned
        select_button = Button(self._root, text="Select",
                               command=self._root.destroy)
        select_button.grid()

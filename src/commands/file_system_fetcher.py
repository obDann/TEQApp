import pandas as pd
from command import Command
from tkinter import *
from tkinter.filedialog import askopenfilename

class FileSystemFetcher(Command):

    def __init__(self, tk_root):
        '''
        (FileSystemFetcher, Tk) -> None

        Initialize the FileSystemFetcher; asks user for an excel file and
        what sheet they would like to upload
        '''
        # REPRESENTATION INVARIANT
        # FileSystemFetcher is a command
        #     it has an OutputQueue
        #     it has an execution status
        # it has a root, a tk object

        # On initialization:
        # there is a boolean called "self._can_exec_flag" which is a flag
        # that determines if file system fetcher can execute

        # if a user selects an excel file and the excel file only has 1 sheet,
        #     self._file is a dictionary that contains a dictonary of
        #     {str: dataframe}
        #     self._the_sheet_name is the determined sheet name

        # if a user selects an excel file with more than 1 sheet
        #     self._file is a dictionary that contains a dictionary of
        #     {str: dataframe}
        #     self._toplevel is a top level frame off of the root
        #     self._selected_sheet is a StringVar to determine what is
        #     the sheet name


        # Initialize an output queue and status
        Command.__init__(self)

        # withdraw the root
        tk_root.withdraw()

        # then initialize the root
        self._root = tk_root

        # get the file system object path
        file_path = self._get_filesystem_object_path()

        # make a "can execute" flag
        self._can_exec_flag = False

        # check if the string is not None
        if file_path:
            # we can assume that there is a successful path selected
            # so we use a dictionary first
            self._file = pd.read_excel(file_path, sheet_name=None)

            # and then we get the sheet names
            self._sheet_names = list(self._file)

            # then check if there is only one sheet
            if (len(self._sheet_names) == 1):
                self._the_sheet_name = self._sheet_names[0]
                # the user can execute fsf
                self._can_exec_flag = True
            elif (len(self._sheet_names) > 1):
                # we create a toplevel using our root
                self._toplevel = Toplevel(self._root)
                # create a selected sheet
                self._selected_sheet = StringVar()
                # we default the dropdown to be the first sheet name of the
                # dropdown
                self._selected_sheet.set(self._sheet_names[0])
                # then we use a sheet selection object for the user to select
                # a sheet
                self._run_selection()


    def execute(self):
        '''
        (FileSystemFetcher) -> DataFrame

        Returns a dataframe that is representative of the excel file.
        Returns None if the user has cancelled halfway through initialization
        '''
        # check if there is one sheet to select from and check if the flag
        # is ready
        if (self._can_exec_flag and len(self._sheet_names) == 1):
            # if it can, set the execution status to true
            self._exec_status = True
            # then return the specified file
            return self._file[self._the_sheet_name]
        # otherwise, check if there is more than 1 sheet
        elif len(self._sheet_names) > 1:
            # if there is, wait for the top level
            self._toplevel.wait_window()
            # then check if the execution status is okay
            if (self._can_exec_flag):
                # if it is okay, then we can return the sheet name
                return self._file[self._the_sheet_name]


    def _get_filesystem_object_path(self):
        '''
        (FileSystemFetcher) -> str

        Returns a string containing the path to an excel file
        '''
        excel_types = [".xlsx", ".xlsm"]
        # set the file types we want
        wanted_filetypes = [('Excel', excel_types)]
        # let the user access the specified file types
        self._root.fileName = askopenfilename(filetypes=wanted_filetypes)
        # then return the path to the file
        return self._root.fileName

    def executed_properly(self):
        '''
        (FileSystemFetcher) -> boolean

        Determines whether or not the FileSystemFetcher was executed
        properly
        '''
        return self._exec_status

    def _run_selection(self):
        '''
        (FileSystemFetcher) -> None

        Let's a user pick out a sheet
        '''
        # ask the user what sheet they would like to pick
        my_text_label = "Which sheet are you going to be uploading?"
        label = Label(self._toplevel, text=my_text_label)
        label.grid()

        # then what is wanted is a dropdown option list
        menu = OptionMenu(self._toplevel, self._selected_sheet,
                          *self._sheet_names)
        menu.grid()

        # then have a select button; once the user presses select, the
        # string is returned
        select_button = Button(self._toplevel, text="Select",
                               command=self._submit)
        select_button.grid()



    def _submit(self):
        '''
        (FileSystemFetcher) -> None

        Determines what happens after a user clicks submit
        '''
        # the person can now execute file system fetcher
        self._can_exec_flag = True
        # set the name of the sheet that is selected
        self._the_sheet_name = self._selected_sheet.get()
        # then destroy the top level
        self._toplevel.destroy()


if __name__ == '__main__':
    tk_root = Tk()
    my_fsf = FileSystemFetcher(tk_root)
    x = my_fsf.execute()
    print(x)
    tk_root.mainloop()

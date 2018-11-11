import pandas as pd
from command import Command
from tkinter import *
from tkinter.filedialog import askopenfilename
from sheet_selection import *

class FileSystemFetcher(Command):

    def __init__(self, tk_root):
        '''
        (FileSystemFetcher, TemplateHandler, Tk) -> None

        Initialize the FileSystemFetcher
        '''
        # REPRESENTATION INVARIANT
        # FileSystemFetcher is a command
        #     it has an OutputQueue
        #     it has an execution status
        # it has a root, a tk object

        # Initialize an output queue and status
        Command.__init__(self)

        # withdraw the root
        tk_root.withdraw()

        # then initialize the root
        self._root = tk_root

        # and initialize the template hanlder
        # self.th = th

    def execute(self):
        '''
        (FileSystemFetcher) -> {str: DataFrame}

        Accesses a file using a User Interface and returns a dictionary of
        DataFrames that maps to a sheet name
        '''
        # get the file system object path
        file_path = self._get_filesystem_object_path()

        # and we can destroy our root here
        self._root.destroy()

        # check if the string is None (the user did not select an excel file)
        if not file_path:
            # create a message
            msg = "An excel file has not been selected."
            # enqueue a the string as an output
            self._opq.enqueue(msg)
            # then return None
            return None

        # otherwise, we can assume that there is a successful path selected
        # so we use a dictionary first
        file = pd.read_excel(file_path, sheet_name=None)

        # and then we get the sheet names
        sheet_names = list(file)

        # check if there is only one sheet
        if (len(sheet_names) == 1):
            # if there is, just return the dataframe selected
            the_sheet_name = sheet_names[0]
            return file[the_sheet_name]
        # otherwise, we check if there are more sheets
        elif (len(sheet_names) > 1):
            # we create another root
            some_root = Tk()
            # create a selected sheet
            selected_sheet = StringVar()
            # we default the dropdown to be the first sheet name of the
            # dropdown
            selected_sheet.set(sheet_names[0])
            # then we use a sheet selection object for the user to select a
            # sheet
            SheetSelection(sheet_names, selected_sheet, some_root)
            some_root.mainloop()
            # then return the selected sheet
            return file[selected_sheet.get()]

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


if __name__ == '__main__':
    tk_root = Tk()
    tk_root.withdraw()
    my_fsf = FileSystemFetcher(tk_root)
    x = my_fsf.execute()
    tk_root.mainloop()

import pandas as pd
from Command import *
from tkinter import Tk
from tkinter.filedialog import askopenfilename


class FileSystemFetcher(Command):

    def __init__(self, tk_root=None):
        '''
        (FileSystemFetcher, Tk) -> None

        Initialize the FileSystemFetcher
        '''
        # REPRESENTATION INVARIANT
        # FileSystemFetcher is a command
        #     it has an OutputQueue
        #     it has an execution status
        # it has a root, a tk object

        # Initialize an output queue and status
        Command.__init__(self)

        # check if there isn't a root
        if not tk_root:
            # if there isn't a root, then we can initialize one
            tk_root = Tk()
            # we don't want an extra window
            tk_root.withdraw()

        # then initialize the root
        self._root = tk_root

    def execute(self):
        '''
        (FileSystemFetcher) -> {str: DataFrame}

        Accesses a file using a User Interface and returns a dictionary of
        DataFrames that maps to a sheet name
        '''
        # get the file system object path
        file_path = self._get_filesystem_object_path()

        # check if the string is None (the user did not select an excel file)
        if not file_path:
            # create a message
            msg = "An excel file has not been selected."
            # enqueue a the string as an output
            self._opq.enqueue(msg)
            # then return None
            return None

        # otherwise, we can assume that there is a successful path selected
        # so we can return the file, but as a dictionary
        file = pd.read_excel(file_path, sheet_name=None)
        # and we can say that this command has been executed properly
        self._exec_status = True
        return file

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

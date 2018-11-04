from uploading_command import UploadingCommand
from command import Command
import tkinter
import pandas as pd

class DuplicateRowChecker(UploadingCommand):
    '''
    An uploading command that checks for duplicate rows in a dataframe
    '''

    def __init__(self, template_name, root=None):
        '''
        (DuplicateRowChecker, str, tk) -> None

        Initializes a DuplicateRowChecker.
        '''
        # call uploading command's init method (for a template name)
        UploadingCommand.__init__(self, template_name)
        # call command's init method (for an output queue and a execution
        # status)
        Command.__init__(self)
        # we will later deal with the root

    def execute(self, df):
        '''
        (DuplicateRowChecker, DataFrame) -> DataFrame

        Returns a DataFrame with all duplicate rows removed
        '''

    def executed_properly(self):
        '''
        (DuplicateRowChecker) -> None

        Returns a boolean to determine if this command was executed properly
        '''
        return self._exec_status

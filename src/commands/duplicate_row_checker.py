from uploading_command import UploadingCommand
from command import Command
import pandas as pd


class DuplicateRowChecker(Command):
    '''
    A command that checks for duplicate rows in a dataframe
    '''

    def __init__(self, df):
        '''
        (DuplicateRowChecker, DataFrame) -> None

        Initializes a DuplicateRowChecker.
        '''
        Command.__init__(self)
        # set our dataframe
        self._df = df

    def execute(self):
        '''
        (DuplicateRowChecker) -> DataFrame

        Returns a DataFrame with all duplicate rows removed
        '''
        # our execution status is now true
        self._exec_status = True

        # check if the dataframe is empty
        if (self._df.empty):
            # if it is, then just return the same dataframe
            return self._df

        # otherwise, if it isn't then let's return a dataframe with the
        # duplicate values dropped
        return self._df.drop_duplicates()

    def executed_properly(self):
        '''
        (DuplicateRowChecker) -> None

        Returns a boolean to determine if this command was executed properly
        '''
        return self._exec_status

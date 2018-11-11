import pandas as pd
import os
from data_not_entered_exception import DataNotEnteredException


class DropdownProcessor():
    '''
    An intermediary to help with dropdown fields for specific data
    '''

    PATH = os.path.dirname(os.path.realpath(__file__)) + "\\dropdown.csv"

    def __init__(self):
        '''
        (DropdownProcessor) -> None

        Initialize a dropdown processor
        '''
        # REPRESENTATION INVARIANT
        # self._intermediary is a pandas' dataframe that holds all possible
        # combinations for dropdown menus in all templates

        # the first row only has the entry "Reference"
        # the first column of the csv path is the name of the columns that
        # have dropdown menus
        # all other data entries are the dropdown options for that row
        self._intermediary = pd.read_csv(self.PATH, index_col=0,
                                         keep_default_na=False)

    def get_options(self, col_name):
        '''
        (DropdownProcessor, str) -> [list of str]

        Returns a list of options for a specific column name

        RAISES DataNotEnteredException if there does not exist metadata
        for the column presented
        '''
        # first, check if there exists a dropdown value as such
        if not (self.is_dropdown(col_name)):
            msg = "'" + col_name + "' is not a dropdown value."
            raise DataNotEnteredException(msg)

        # otherwise, if it is, then we can get the options from the specified
        # row of the data
        options = self._intermediary.loc[col_name]
        # then we want to remove any trailing NAs
        options = list(options)
        options = filter(None, options)
        return list(options)

    def is_dropdown(self, col_name):
        '''
        (DropdownProcessor, str) -> bool

        Determines if the column name is a dropdown column
        '''
        # check if the column name is in the index
        return col_name in self._intermediary.index

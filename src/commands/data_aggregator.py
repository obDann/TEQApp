import pandas as pd
import numpy as np
import re
from command import Command
from uploading_command import UploadingCommand


class DataAggregator(UploadingCommand):

    def __init__(self, template_name):
        '''
        (DataAggregator, str) -> None

        Initializes a data aggregator, and injects a specific template
        name to the uploading command
        '''
        UploadingCommand.__init__(self, template_name)

    def execute(self, df):
        '''
        (Command, DataFrame) -> DataFrame

        Executes the command, assuming a dataframe object gets passed in.
        Currently only checks for if the data matches the type the column is
        suppose to be.
        '''

        # Gets the column names to a list
        column_name = df.columns.T.tolist()

        for column in column_name:
            # Gets the type that the column is suppose to be in
            # object(string),float or int
            col_type = df[column].dtype.kind
            try:
                # Make sure all the data are the same type as the column
                df[column].get_values().astype(col_type)
            except ValueError:
                # If a string is entered into a set of numeric data
                if (type == np.dtype(int) or type == np.dtype(float)):
                    # The value is set to 0
                    df[column] = df.replace({column: r'[a-zA-z]*'},
                                            {column: 0}, regex=True)
        return df

    def executed_properly(self):
        '''
        (Command) -> boolean

        Returns a boolean to determine if this command was executed properly
        '''
        return self._exec_status

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

    def execute(self, df, th):
        '''
        (Command, DataFrame) -> DataFrame

        Executes the command, assuming a dataframe object gets passed in.
        Currently only checks for if the data matches the type the column is
        suppose to be.
        '''
        template = th.get_template(self._template_name)
        # Gets the column names to a list
        column_name = template.get_mandatory_headers()
        self._exec_status = False
        
        for column in column_name:
            if (column == "Postal_Code"):
                new_col = self.postal_code_checker(df[column])
                df.update(new_col)
            else:
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
        self._exec_status = True        
        return df

    def postal_code_checker(self, df):
            '''
            (DataFrame) ->  DataFrame
            The DataFrame of 'Postal_Code' is given, then return a new
            'Postal_Code' DataFrame to fix any mismatch types of Canadian
            Postal Code. The only form that is right is'X1X1X1'. If there is
            data that is not the correct format, it will be replaced by an
            empty string.
            '''
            p_codes = list()
            # Initalize the regex
            p = re.compile('^([a-zA-z]?[0-9]){3}$')
            for value in df.get_values():
                # Get the value (string)
                postal_code = value
                postal_code = postal_code.replace('-', '')
                postal_code = postal_code.replace(' ', '')
                # Check if the given data matches the type
                if (len(postal_code) == 6 and p.match(postal_code)):
                    p_codes.append(postal_code)
                else:
                    # An empty string replaces the false data
                    p_codes.append("")

            new_df = {'Postal_Code': p_codes}
            return pd.DataFrame(new_df)

    def executed_properly(self):
        '''
        (Command) -> boolean

        Returns a boolean to determine if this command was executed properly
        '''
        return self._exec_status

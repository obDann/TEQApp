import pandas as pd
import numpy as np
import re
from uploading_command import UploadingCommand
import datetime


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
        now = datetime.datetime.now()
        #template = th.get_template(self._template_name)
        # Gets the column names to a list
        #header_name = template.get_header()
        header_name = ['Processing Detail','col2','Postal Code']
        # Gets the list of regex
        #regex = template.get_regex()
        regex = ['','','([A-Z]\d){3}']
        #str(now.year)+'/'+str(now.month)+"/"+str(now.day) 
        
        self._exec_status = False
        
        for header in range(len(header_name)):
            count = 0
            column = df.get(header_name[header])
            if (column is not None):
                for row in range(len(df.index)):
                    # getting the regex from the list
                    p = re.compile(regex[count])
                    # Checks each row for matching regex
                    if (not p.Processingmatch(column[row])):
                        # Automation fix for postal code
                        if (header_name[header] == "Postal Code"):
                            new_col = self.postal_code_checker(column)
                            df.update(new_col)
                        # Automation fix for processing detail
                        elif (header_name[header] == "Processing Detail"):
                            df.replace(df.loc(header, row),str(now.year)+'/'
                                       +str(now.month)+"/"+str(now.day))
                        else:
                            # Open GUI for user to change
                            print("Open GUI")
            # Shift the regex list down by 1 each column is done
            count = count + 1
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

if __name__ == "__main__":
    test = DataAggregator("test")
    df = {'Processing Detail': [1,2,3], 'col2' : [9,2,5], 'Postal Code': ['M1M1M1','Y8Y8Y8']}
    df = pd.Dataframe(df)
    test.execute(df,'template handler')
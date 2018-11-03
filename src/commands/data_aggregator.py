import pandas as pd
import numpy as np
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
        (Command, DataFrame) -> Abstract
        
        Executes the command, assuming a dataframe object gets passed in.
        '''
        df = pd.DataFrame(df)
        
        # Gets the column names to a list
        column_name = df.columns.T.tolist()       
        
        # Gets the data in each column to a list
        column_values = df.values.T.tolist()
        print(column_name)
        print(column_values)
        
        for column in column_name:
            # Gets the type that the column is suppose to be
            # O = object (string), f = float, i = int
            type = df[column].dtype.kind    
            df[column].replace(' ', 'Hi')
     
    def executed_properly(self):
        '''
        (Command) -> boolean
        
        Returns a boolean to determine if this command was executed properly
        '''
        return self._exec_status
    
if __name__ == "__main__":
    some_command = DataAggregator('template name')
    df = {'float': [1.66, 20.91], 'int': [3, 4], 'string' : ["test", " "]}
    some_command.execute(df)
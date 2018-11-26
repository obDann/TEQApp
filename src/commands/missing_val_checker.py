import pandas as pd
from uploading_command import UploadingCommand
import sys
sys.path.append("../temhelp")
from template_handler import TemplateHandler

class MissingValChecker(UploadingCommand):

    def __init__(self, template_name):
        ''' (MissingValChecker, Dataframe, TemplateHandler) -> None

        Initializes a MissingValChecker object with it's dataframe to
        parse and TemplateHandler to reference
        '''
        UploadingCommand.__init__(self, template_name)

    def execute(self, df, template):
        '''
        (MissingValChecker, DataFrame, TemplateHandler) -> DataFrame
        
        Given a MissingValChecker object parses the DataFrame and allows the
        user to enter values into the empty mandatory fields, then returns
        the fixed DataFrame
        '''
        self._exec_status = False
        
        empty_fields = parse_columns(df, template)

        self._exec_status = True
        
        return df

    def executed_properly(self):
        '''
        (Command) -> boolean

        Returns a boolean to determine if this command was executed properly
        '''
        return self._exec_status

def parse_columns(df, template):
    '''
    (DataFrame, TemplateHandler) -> List of [Tuple of (String, int)]

    Given a DataFrame and TemplateHandler, returns a tuple of all empty
    mandatory fields as in the TemplateHandle

    If an entire column is missing, row will be set to -1
    Row is 0 indexed
    '''
    mandatory_headers = template.get_mandatory_headers()
    missing_fields = []

    # append to missing_fields any missing mandatory fields
    for header in mandatory_headers:
        column = df.get(header)
        if not df.empty and column is not None:
            for row in range(len(df.index)):
                field = df.iloc[row:row+1][header]
                if (empty_field(field)):
                    missing_fields.append((header, row))
        else:
            missing_fields.append((header, -1))

    return missing_fields

def empty_field(df):
    ''' (DataFrame) -> boolean
    
    Given a DataFrame with 1 field, returns True if the DataFrame
    is empty or the only value is an empty string, otherwise returns
    False
    '''
    is_empty = df.isna().any()
    empty_string = (isinstance(df.iat[0], str) and df.iat[0] == "")
    return is_empty or empty_string

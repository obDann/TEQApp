import pandas as pd
#from uploading_command import *
from src import TemplateHeader

class MissingValChecker():

    def __init__(self, df, TemplateHandler):
        ''' (MissingValChecker, Dataframe, TemplateHandler) -> None
        
        Initializes a MissingValChecker object with it's dataframe to
        parse and TemplateHandler to reference
        '''
        self.df = df;
        self.template = TemplateHandler;
        

    def parse_column(self):
        ''' (MissingValChecker) -> List of [Tuple of (String, int)]
        
        Given a MissingValChecker object parses its dataframe and returns
        a tuple of all empty mandatary fields as in the TemplateHandle
        '''
        mandatory_headers = self.template.get_mandatary_headers()
        missing_fields = []
        for header in mandatory_headers:
            column = df.get(header)
            if column is not None:
                for row in range(len(df.index)):
                    if (df.get(header)[row].isnull()):
                        missing_fields.append([header, row])
            else:
                missing_fields.append([header, -1])
        
        return missing_fields
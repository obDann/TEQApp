import pandas as pd
from Command import *

class UploadMissingValueChecker():
    
    def __init__(self):
        pass
     
    def get_headers(self, file):
        ''' (UploadMissingValueChecker, DataFrame) -> List
        
        Given a DataFrame object returns a list of headers
        '''
        return file.columns.values.tolist();
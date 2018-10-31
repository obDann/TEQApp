import pandas as pd
from Command import *

class MissingValChecker():

    def __init__(self):
        pass

    def get_headers(self, file):
        ''' (MissingValChecker, DataFrame) -> List

        Given a DataFrame object returns a list of headers
        '''
        return file.columns.values.tolist();
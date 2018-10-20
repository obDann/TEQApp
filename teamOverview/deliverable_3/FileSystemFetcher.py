import pandas as pd;
from xlrd import open_workbook, XLRDError

def execute(file_path, sheet=0):
    ''' (str, int) -> DataFrame
    Given the absolute or relative path to an excel file,
    returns the DataFrame object
    '''
    if (is_excel(file_path)):
        file = pd.read_excel(file_path, sheet)
        return file
    return None

def is_excel(file_path):
    ''' (str) -> bool
    Given a string, returns True if it is an absolute or
    relate path to an excel file, otherwise returns False
    '''
    try:
        open_workbook(file_path)
    except:
        return False
    return True

# addtional functions if later required
"""
def get_row(file, row):
    row = file.iloc[row-1:row]
    return row

def get_field(file, row, column):
    row = file.iloc[row-1:row, column-1:column]
    return row

def get_column_field(file, column, index):
    return file[column].iloc[index-1]
"""
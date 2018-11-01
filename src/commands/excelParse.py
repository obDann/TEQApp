import pandas as pd
import os

# type 'pip install pandas' in the command line to install the pandas module

def parse(ex_data):
    '''
    (DataFrame) -> ([list of column headers],[list of lists containing values])

    Takes a DataFrame as its parameter and parses the file.
    Outputs a tuple where the first value is a list of the column headers and
    the second value is another list with each index corresponding to the
    column header of the first list. Inside this list is another set of lists
    where the column values are held.
    '''
    # pd.read_excel(ex_data) parses an excel file to get a DataFrame
    # ex_data = pd.DataFrame(test) changes type of dictionary to DataFrame

    # gets the column headers and puts them into a list
    columns = ex_data.columns.values.tolist()

    values = list()
    for header in range(0, len(columns)):
        # gets a list of the values under the column header
        values.append(ex_data[columns[header]].tolist())

    # ex_data.describe() gives summary statistics for numerical columns only

    return (columns, values)

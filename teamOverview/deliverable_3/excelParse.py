# https://pypi.org/project/xlrd/ <-- reference page for xlrd, not pandas
# type 'pip install pandas' in the command line to install the pandas module
import pandas
import os

def parse(excel):
    '''
    Takes an excel file as its parameters (can also take an open file object)
    and parses the file. Outputs a tuple where the first value is a list of
    the column headers and the second value is another list with each index
    corresponding to the column header of the first list. Inside this list
    is another set of lists where the column values are held.
    (file) -> ([list of column headers], [list of lists containing values])
    '''
    ex_data = pandas.read_excel(excel)
    
    # gets the column headers and puts them into a list
    columns = ex_data.columns.values.tolist()

    values = list()
    for header in range(0, len(columns)):
        # gets a list of the values under the column header
        values.append(ex_data[columns[header]].tolist())
    
    # ex_data.describe() gives summary statistics for numerical columns only    
    
    return (columns, values)


if __name__ == "__main__":
    # location of excel file in same directory
    __location__ = os.path.realpath(os.path.join(os.getcwd(), "test.xlsx"))
    parsed = parse(__location__)
    print(parsed)

import sqlite3
import database_methods
import insert_data_functions
import pandas as pd

def insert_address(df, row_values):
    '''
    Grabs a row and inserts the data for a row in the Address table.
    Takes in a dataframe read_excel object and iloc[row] object.
    '''
    address_id = database_methods.get_id("Address") + 1
    val = [address_id]
    # fetch column values 7-15 which correspond to the address values
    val = database_methods.fetch_values(7, 15, row_values, val)
    # insert into table
    insert_data_functions.insert_row(val, "Address")
    
    return address_id

def insert_client(df, row_values, address_id, agency):
    '''
    Inserts data into the Client table. Takes in a dataframe read_excel 
    object, iloc[row] object, address id, and agency name.
    '''
    # get the values of columns 0-6
    v1 = database_methods.fetch_values(0, 7, row_values, [])
    # get the values of columns 16-17
    val = database_methods.fetch_values(15, 17, row_values, v1)
    # add address_id and agency
    val.append(address_id)
    val.append(agency)
    
    insert_data_functions.insert_row(val, "Client")

    
    
    
    
    
    
    
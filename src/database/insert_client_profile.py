import sqlite3
import database_methods
import insert_general
import insert_helper
import pandas as pd

def insert_address(row_values):
    '''
    Grabs a row and inserts the data for a row in the Address table.
    Takes in a dataframe read_excel object with iloc[row].
    '''
    add_id = insert_general.insert_address(row_values, [(7, 15)])
    
    return add_id

def insert_client(row_values, address_id, agency):
    '''
    Inserts data into the Client table. Takes in a dataframe read_excel 
    object with iloc[row], address id, and agency name.
    '''
    # get the values of columns 0-6
    v1 = database_methods.fetch_values(0, 7, row_values, [])
    # get the values of columns 16-17
    val = database_methods.fetch_values(15, 17, row_values, v1)
    # add address_id and agency
    val.append(address_id)
    val.append(agency)
    
    insert_helper.insert_row(val, "Client")

    
    
    
    
    
    
    
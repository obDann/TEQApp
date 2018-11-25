import sqlite3
import database_methods
import insert_general
import insert_helper
import pandas as pd

def insert_address(column_values, row_values):
    '''
    Grabs a row and inserts the data for a row in the Address table.
    Takes in a dataframe read_excel object with iloc[row].
    '''
    # check if client exists in the database
    client_id = row_values[2]
    index_list = [(7, 15)]
    if (not(database_methods.check_id(client_id, 'client_data.db', "Client",
                                      "Unique_ID_Value"))):
        add_id = insert_general.insert_address(row_values, index_list)
        return add_id
    else:
        # if customer already exists, update their address with current data
        lst = ["Street_Number", "Street_Name", "Street_Type", 
               "Street_Direction", "Unit", "City", "Province", "Postal_Code"]
        (col, data) = database_methods.update_lists(lst, column_values, 
                                                    row_values, index_list)
        add_id = database_methods.get_existing_id("client_data.db", "Client",
                                                  "Address_ID",
                                                  "Unique_ID_Value", client_id)
        query = database_methods.create_update_query(col, data, "Address", 
                                                     "ID", add_id)
        database_methods.update_query(query, "client_data.db")
        

def insert_client(column_values, row_values, address_id):
    '''
    Inserts data into the Client table. Takes in a dataframe read_excel 
    object with iloc[row], address id, and agency name.
    '''
    # get client id and check if it exists in the database, if not
    # insert the client
    client_id = row_values[2]
    if (not(database_methods.check_id(client_id, 'client_data.db', "Client",
                                      "Unique_ID_Value"))):
        # get the values of columns 0-6
        v1 = database_methods.fetch_values(0, 7, row_values, [])
        # get the values of columns 16-17
        val = database_methods.fetch_values(15, 17, row_values, v1)
        # add address_id
        val.append(address_id)
    
        insert_helper.insert_row(val, "Client")
    else:
        #if client already exists in the database, update their data
        lst = ["Processing_Details", "Date_Of_Birth", "Phone", "Email",
               "Email_Address", "Official_Language_Preference", 
               "Consent_Future"]
        index_list = [(0, 1), (3, 7), (15, 17)]
        (col, data) = database_methods.update_lists(lst, column_values, 
                                                    row_values, index_list)
        query = database_methods.create_update_query(col, data, "Client", 
                                                     "Unique_ID_Value",
                                                     client_id)
        database_methods.update_query(query, "client_data.db")

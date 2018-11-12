import sqlite3
import database_methods
import insert_helper
import pandas as pd

#Tables that are shown in several iCare files
def insert_address(row_values, index):
    address_id = database_methods.get_id("Address") + 1
    val = [address_id]
    val = database_methods.fetch_values_list(row_values, index, val)
    # insert into table
    insert_helper.insert_row(val, "Address")
    
    return address_id

def insert_service(row_values, skill_idx, service_type):
    '''
    Insert a row in the Service table.
    '''
    service_id = database_methods.get_id("Service") + 1
    val = [service_id]
    val = database_methods.fetch_values(skill_idx, skill_idx + 1, 
                                        row_values, val)
    val.append(service_type)
    insert_helper.insert_row(val, "Service")
    
    return service_id

def insert_client_service(service_id, client_id, month, year):
    '''
    Inserts a row in the Client_Attends_Service table.
    '''
    val = [service_id, client_id, month, year]
    if (database_methods.check_id(client_id, 'client_data.db', "Client",
                                      "Unique_ID_Value") and 
        database_methods.check_id(service_id, 'client_data.db', "Service",
                                              "ID")): 
        insert_helper.insert_row(val, "Client_Attends_Service")
    
def insert_target_group(row_values, start, end):
    '''
    Insert a row into the Target_Group table.
    '''
    # get id to insert
    target_id = database_methods.get_id("Target_Group") + 1
    val = [target_id]
    val = database_methods.fetch_values(start, end, row_values, val)
    insert_helper.insert_row(val, "Target_Group")
    
    return target_id

def insert_3_value(column_values, row_values, table, item_id, start, end):
    '''
    For inserting tables with (id, column_name, value) rows.
    '''
    i = start
    while (i < end):
        val = [item_id]
        if (type(row_values[i]) == str and row_values[i] != "N/A"):
            val.append(column_values[i])
            val.append(row_values[i])
            insert_helper.insert_row(val, table)
        i += 1
import sqlite3
import database_methods
import insert_helper
import insert_general
import pandas as pd

db = 'client_data.db'

def insert_target(row_values):
    # check if direct at target group field is Yes
    if (row_values[17] == "Yes"):
        target_id = insert_general.insert_target_group(row_values, 18, 32)
        return target_id
    
    return None

def insert_service(row_values):
    service_id = insert_general.insert_service(row_values, 37, 
                                               "Community Connections")
    
    return service_id
    
def insert_community_conn(row_values, service_id, target_id):
    '''
    Inserts a row in the Community_Connections table.
    '''
    val = [service_id, target_id]
    index = [(5, 7), (8, 17), (32, 37), (65, 67)]
    val = database_methods.fetch_values_list(row_values, index, val)
    
    insert_helper.insert_row(val, "Community_Connections")

def client_attends_service(service_id, client_id, month, year):
    insert_general.insert_client_service(service_id, client_id, month, year)

def insert_skills(column_values, row_values, client_id):
    '''
    Inserts clients skills into the Skills table.
    '''
    index_list = [(38, 44)]
    if (database_methods.check_id(client_id, 'client_data.db', "Client",
                                      "Unique_ID_Value")):    
        insert_general.update_skills(column_values, row_values, client_id, 
                                     index_list)

def update_client_profile(client_id, row_values):
    index_list = [(0, 1), (4, 5), (7, 8)]
    if (database_methods.check_id(client_id, 'client_data.db', "Client",
                                      "Unique_ID_Value")):    
        insert_general.update_client_profile(row_values, client_id, index_list)

def update_child(row_values, client_id):
    lst = ["Age", "Type_Of_Care"]
    table = "Child"
    prim = "(Client_Unique_ID_Value, Child)"
    if (database_methods.check_id(client_id, 'client_data.db', "Client",
                                      "Unique_ID_Value")):  
        insert_general.update_child(row_values, client_id, lst, table, prim, 1,
                                    46, 55)
import sqlite3
import database_methods
import insert_helper
import insert_general
import pandas as pd

def insert_target(row_values):
    # check if direct at target group field is Yes
    if (row_values[17] == "Yes"):
        target_id = insert_general.insert_target_group(row_values, 18, 32)
        return target_id
    
    return 0

def insert_service(row_values):
    service_id = insert_general.insert_service(row_values, 37, 
                                               "Community Connections")
    
    return service_id
    
def insert_community_conn(row_values, service_id, target_id):
    '''
    Inserts a row in the Community_Connections table.
    '''
    val = [service_id, target_id]
    index = [(9, 10), (11, 17), (32, 37), (65, 67)]
    val = database_methods.fetch_values_list(row_values, index, val)
    
    insert_helper.insert_row(val, "Community_Connections")

def insert_skills(column_values, row_values, client_id):
    '''
    Inserts clients skills into the Skills table.
    '''
    insert_general.insert_3_value(column_values, row_values, 
                                 "Skills", client_id, 38, 44)
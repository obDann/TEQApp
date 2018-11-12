import sqlite3
import database_methods
import insert_helper
import insert_general
import pandas as pd

def insert_target(row_values):
    # check if direct at target group field is Yes
    if (row_values[16] == "Yes"):
        target_id = insert_general.insert_target_group(row_values, 17, 31)
        return target_id
    
    return None

def insert_service(row_values):
    service_id = insert_general.insert_service(row_values, 63, 
                                               "Information & Orientation")
    
    return service_id


def insert_skills(column_values, row_values, client_id):
    '''
    Inserts rows in Skills table.
    '''
    insert_general.insert_3_value(column_values, row_values, 
                                  "Skills", client_id, 64, 69)
    insert_general.insert_3_value(column_values, row_values, 
                                  "Skills", client_id, 70, 71)

def insert_info_and_ori(row_values, service_id, target_id):
    '''
    Inserts a row in the Info_and_Orientation table.
    '''
    index = [(6, 7), (11, 16), (69, 70), (93, 94)]
    val = [service_id, target_id]
    val = database_methods.fetch_values_list(row_values, index, val)
    
    insert_helper.insert_row(val, "Info_and_Orientation")

def client_attends_service(service_id, client_id, month, year):
    insert_general.insert_client_service(service_id, client_id, month, year)

def insert_service_needs(column_values, row_values, service_id):
    '''
    Inserts rows into the Service_Needs table.
    '''
    if (not(database_methods.check_id(service_id, 'client_data.db', 
                                      "Service_Needs", "Service_ID"))):    
        insert_general.insert_3_value(column_values, row_values, 
                                      "Service_Needs", service_id, 31, 63)
        insert_general.insert_3_value(column_values, row_values, 
                                      "Service_Needs", service_id, 71, 72)
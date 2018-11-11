import sqlite3
import database_methods
import insert_helper
import insert_general
import pandas as pd

def insert_service(row_values):
    # grabs row 29
    service_id = insert_general.insert_service(row_values, 29, "Employment")
    return service_id

def insert_skills(column_values, row_values, client_id):
    # client skills
    insert_general.insert_3_value(column_values, row_values, 
                                  "Skills", client_id, 30, 36)
    
def insert_employment(row_values, service_id):
    '''
    Inserts a row in the Employment_Service table.
    '''
    index = [(6, 8), (12, 18), (66, 68)]
    val = [service_id]
    val = database_methods.fetch_values_list(row_values, index, val)
    
    insert_helper.insert_row(val, "Employment_Service")

def insert_long_term(row_values, service_id):
    '''
    Inserts a row in the Long_Term_Intervention table.
    '''
    long_term_id = database_methods.get_id("Long_Term_Intervention") + 1
    val = [long_term_id, service_id]
    # check if long term intervention was recieved
    if (type(row_values[18]) == str):
        val = database_methods.fetch_values(18, 29, row_values, val)
        insert_helper.insert_row(val, "Long_Term_Intervention")

def insert_short_term(row_values, service_id):
    '''
    Inserts a row in the Short_Term_Intervention table.
    '''
    i = 36
    end = 44
    while (i < end):
        short_term_id = database_methods.get_id("Short_Term_Intervention") + 1
        val = [short_term_id, service_id]
        # check if short term intervention received column is not empty
        if (type(row_values[i]) == str):
            val.append(row_values[i])
            val.append(row_values[i+1])
            insert_helper.insert_row(val, "Short_Term_Intervention")
        i += 2

def client_attends_service(service_id, client_id, month, year):
    insert_general.insert_client_service(service_id, client_id, month, year)
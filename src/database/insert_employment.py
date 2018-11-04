import sqlite3
import database_methods
import insert_helper
import insert_general
import pandas as pd

def insert_service(row_values):
    service_id = insert_general.insert_service(row_values, 29, "Employment")
    return service_id

def insert_skills(column_values, row_values, client_id):
    insert_general.insert_3_value(column_values, row_values, 
                                  "Skills", client_id, 30, 36)
    
#def insert_employment():

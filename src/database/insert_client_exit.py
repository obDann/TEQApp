import sqlite3
import database_methods
import insert_helper
import insert_general
import pandas as pd

def insert_client_exit(row_values, client_id, course_code):
    index = [(6, 9), (13, 16)]
    val = [client_id, course_code]
    val = database_methods.fetch_values_list(row_values, index, val)
    
    insert_helper.insert_row(val, "Client_Exit")

def insert_CLB_level(column_values, row_values, client_id, course_code):
    # check if any CLB levels are filled in
    i = 9
    while (i < 13):
        val = [client_id, course_code]
        if (type(row_values[i]) == str):
            val.append(column_values[i])
            val.append(row_values[i])
            insert_helper.insert_row(val, "Client_CLB_Level")
        i += 1
            
            
import sqlite3
import database_methods
import insert_helper
import insert_general
import pandas as pd

def insert_client_enrol(row_values, client_id, course_code):
    val = [course_code, client_id]
    val.append(row_values[7])
    
    insert_helper.insert_row(val, "Client_Enrolment")
import sqlite3
import database_methods
import insert_helper
import insert_general
import pandas as pd

def insert_client_enrol(row_values, client_id, course_code):
    key = (course_code, client_id) 
    # check if client id and course code exists in the database
    if ((database_methods.check_id(client_id, 'client_data.db', "Client",
                                      "Unique_ID_Value")) and
        (database_methods.check_course(course_code, 'client_data.db')) and           
        (not(database_methods.check_id(key, 'client_data.db', "Client_Enrolment",
                                   ("(Course_Code, " + 
                                    "Client_Unique_ID_Value)"))))):
        val = [course_code, client_id]
        val.append(row_values[7])        
        insert_helper.insert_row(val, "Client_Enrolment")
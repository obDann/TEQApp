import sqlite3
import database_methods
import insert_general
import insert_helper
import pandas as pd

db = 'client_data.db'

def insert_client(column_values, row_values, id_value, agency):
    '''
    Check if client has a row in Client table (aka client has filled out the
    Client Profile file). If not, insert missing data into Client table.
    '''
    # if client did not submit client profile form
    if (not(database_methods.check_id(id_value, db, "Client",
                                      "Unique_ID_Value"))):
        # extract the data and insert a row into Client table
        index = [(0, 1), (2, 5), (8, 9)]
        val = database_methods.fetch_values_list(row_values, index, [])
        val.append(agency)
        # insert into Client table
        query = ("INSERT INTO Client (Processing_Details, Unique_ID_Type, " + 
                 "Unique_ID_Value, Date_Of_Birth, Official_Language_Preference"
                 + ", Agency) VALUES (?, ?, ?, ?, ?, ?);")

        database_methods.execute_query(query, val, 'client_data.db')
    else:
        # if client is in the database, update data
        lst = ["Processing_Details", "Date_Of_Birth", 
               "Official_Language_Preference"]
        index_list = [(0, 1), (4, 5), (8, 9)]
        (col, data) = database_methods.update_lists(lst, column_values, 
                                                    row_values, index_list)
        query = database_methods.create_update_query(col, data, "Client", 
                                                     "Unique_ID_Value",
                                                     id_value)
        database_methods.update_query(query, db)        
        
    
def insert_referral(column_values, row_values, id_value, agency):
    '''
    Inserts data into the Referral table. Gets client unique identifier value
    and a dataframe read_excel object with iloc[row]. Returns 1 if information
    has been inserted and 0 otherwise.
    '''
    # check client has been inserted already
    insert_client(column_values, row_values, id_value, agency)
    index = [(1, 2), (5, 8), (9, 11), (39, 41), (47, 48), (68, 69), 
             (89, 92)]    
    if (not(database_methods.check_id(id_value, db, "Referral",
                                      "Client_Unique_ID_Value"))):    
        val = [id_value]
        val = database_methods.fetch_values_list(row_values, index, val)

        insert_helper.insert_row(val, "Referral")
        return 1
    else:
        # client has been inserted, update data
        lst = ["Update_Record_ID", "Service_Postal_Code", 
               "Assessment_Start_Date", "Service_Language", 
               "Where_Service_Received", "Referred_By", 
               "Canadian_Citizen_Intention", "Support_Services_Required",
               "Non_IRCC_Services", "Support_Services_Received",
               "Settlement_Plan_Completed", "Assessment_End_Date",
               "Reason_For_Update"]
        (col, data) = database_methods.update_lists(lst, column_values, 
                                                    row_values, index)
        query = database_methods.create_update_query(col, data, "Referral", 
                                                     "Client_Unique_ID_Value",
                                                     id_value)
        database_methods.update_query(query, db)        
    
    return 0

def new_child(row_values, id_value):
    '''
    Inserts child information in the Child table.
    '''
    # check child fields are not empty and insert
    i = 1
    j = 70   
    while (j < 79):
        if (type(row_values[j]) == str or type(row_values[j+1]) == str):
            val = [id_value, i]
            val = database_methods.fetch_values(j, j+2, row_values, val)
            insert_helper.insert_row(val, "Child")
        i += 1
        j += 2

def insert_child(row_values, id_value):
    lst = ["Age", "Type_Of_Care"]
    table = "Child"
    prim = "(Client_Unique_ID_Value, Child)"
    insert_general.update_child(row_values, id_value, lst, table, prim, 1, 
                                70, 79)

def insert_trans_int(row_values, id_value):
    '''
    Inserts information in the Translation_Interpretation table.
    '''
    table = "Translation_Interpretation"
    prim = "(Client_Unique_ID_Value, Type)"
    trans_id = ("(" + id_value + ", 'Translation')")
    int_id = ("(" + id_value + ", 'Interpretation')")
    val = [id_value]
    lst = ["'Between'", "'And'"]
    # check if "Translation" is Yes
    if (row_values[82] == "Yes"):
        value = database_methods.get_existing_id(db, table, "Type", prim, 
                                                 trans_id)
        if (value is not None):
            (col, data) = database_methods.update_lists(lst, None, 
                                                        row_values, [(83, 85)])
            query = database_methods.create_update_query(col, data, table, prim,
                                                         trans_id)
            database_methods.update_query(query, db)
        else:
            val.append("Translation")
            # get columns 83-84
            val = database_methods.fetch_values(83, 85, row_values, val)
            insert_helper.insert_row(val, table)
    
    val = [id_value]
    # check if "Interpretation" is Yes
    if (row_values[85] == "Yes"):
        value = database_methods.get_existing_id(db, table, "Type", prim, 
                                                 int_id)
        if (value is not None):
            (col, data) = database_methods.update_lists(lst, None, 
                                                        row_values, [(86, 88)])
            query = database_methods.create_update_query(col, data, table, prim,
                                                         int_id)
            database_methods.update_query(query, db)
        else:
            val.append("Interpretation")
            val = database_methods.fetch_values(86, 88, row_values, val)
            insert_helper.insert_row(val, table)
        
def insert_find_employment(row_values, id_value):
    '''
    Inserts data into the Find_Employment table.
    '''
    val = [id_value]
    table = "Find_Employment"
    prim = "Client_Unique_ID_Value"
    lst = ["Find_Employment_R", "Timeframe", "Min_One_Year_Exp", 
           "NOC_Level_Intention", "Obtain_Credentials_License"]
    # check if "Find employment" column is "Yes"
    if (row_values[33] == "Yes"):
        value = database_methods.check_id(id_value, db, table, prim)
        if (value == 1):
            (col, data) = database_methods.update_lists(lst, None, 
                                                        row_values, [(34, 39)])
            query = database_methods.create_update_query(col, data, table, prim,
                                                         id_value)
            database_methods.update_query(query, db)
        else:
            # get columns 34-38
            val = database_methods.fetch_values(34, 39, row_values, val)
            insert_helper.insert_row(val, table)

def insert_improve_skills(column_names, row_values, id_value):
    '''
    Inserts data into the Improve_Skills table.
    '''
    val = [id_value]
    table = "Improve_Skills"
    prim = "(Client_Unique_ID_Value, Improve)"
    lst = ["'Description'"]
    if (type(row_values[29]) == str):
        prim_val = "(" + id_value + ", '" + column_names[29] + "')"
        value = database_methods.get_existing_id(db, table, "Improve", prim, 
                                                 prim_val)
        if (value is not None):
            (col, data) = database_methods.update_lists(lst, None, row_values, 
                                                        [(29, 30)])
            query = database_methods.create_update_query(col, data, table, prim,
                                                         prim_val)
            database_methods.update_query(query, db)
        else:
            val.append(column_names[29])
            val = database_methods.fetch_values(29, 30, row_values, val)
            insert_helper.insert_row(val, table)
    
    val = [id_value]
    if (type(row_values[32]) == str):
        prim_val = "(" + id_value + ", '" + column_names[32] + "')"
        value = database_methods.get_existing_id(db, table, "Improve", prim, 
                                                 prim_val)
        if (value is not None):
            (col, data) = database_methods.update_lists(lst, None, row_values, 
                                                        [(32, 33)])
            query = database_methods.create_update_query(col, data, table, prim,
                                                         prim_val)
            database_methods.update_query(query, db)
        else:
            val.append(column_names[32])
            val = database_methods.fetch_values(32, 33, row_values, val)
            insert_helper.insert_row(val, table)        

def insert_client_needs(column_values, row_values, id_value):
    '''
    Inserts data into the Client_Needs table. Values are all Yes/No
    '''
    index_list = [(11, 29), (30, 32), (33, 34), (41, 47), (48, 68)]
    table = "Client_Needs"
    prim = "(Client_Unique_ID_Value, Type)"
    lst = ["Value"]
    i = 0
    while (i < len(index_list)):
        start = index_list[i][0]
        end = index_list[i][1]
        while (start < end):
            if (type(row_values[start] == str)):
                prim_val = "(" + id_value + ", '" + column_values[start] + "')"
                value = database_methods.get_existing_id(db, table, "Type", 
                                                         prim, prim_val)
                if (value is not None):
                    (col, data) = database_methods.update_lists(lst, None, 
                                                                row_values, 
                                                                [(start, 
                                                                  start + 1)])
                    query = database_methods.create_update_query(col, data, 
                                                                 table, prim,
                                                                 prim_val)
                    database_methods.update_query(query, db)
                else:
                    insert_general.insert_3_value(column_values, row_values, 
                                                  table, id_value, start, 
                                                  start + 1)
            start += 1
        i += 1
    
#if __name__ == "__main__":
    #df = pd.read_excel('file.xlsx')
    #column_values = df.iloc[1]
    #row_values = df.iloc[2]
import sqlite3
import database_methods
import insert_general
import insert_helper
import pandas as pd

def insert_client(row_values, id_value, agency):
    '''
    Check if client has a row in Client table (aka client has filled out the
    Client Profile file). If not, insert missing data into Client table.
    '''
    # if client did not submit client profile form
    if (not(database_methods.check_client(id_value, 'client_data.db'))):
        # extract the data and insert a row into Client table
        index = [(0, 1), (2, 5), (8, 9)]
        val = insert_general.insert(row_values, index, [])
        val.append(agency)
        # insert into Client table
        query = ("INSERT INTO Client (Processing_Details, Unique_ID_Type, " + 
                 "Unique_ID_Value, Date_Of_Birth, Official_Language_Preference"
                 + ", Agency) VALUES (?, ?, ?, ?, ?, ?);")

        database_methods.execute_query(query, val, 'client_data.db')
        
    
def insert_referral(row_values, id_value, agency):
    '''
    Inserts data into the Referral table. Gets client unique identifier value
    and a dataframe read_excel object with iloc[row].
    '''
    # check client has been inserted already
    insert_client(id_value, agency, row_values)
    index = [(1, 2), (5, 8), (9, 11), (39, 41), (47, 48), (68, 69), (89, 92)]
    val = [id_value]
    val = insert_general.insert(index, row_values, val)

    insert_helper.insert_row(val, "Referral")

def insert_child(row_values, id_value):
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

def insert_trans_int(row_values, id_value):
    '''
    Inserts information in the Translation_Interpretation table.
    '''
    val = [id_value]
    # check if "Translation" is Yes
    if (row_values[82] == "Yes"):
        val.append("Translation")
        # get columns 83-84
        val = database_methods.fetch_values(83, 85, row_values, val)
        insert_helper.insert_row(val, "Translation_Interpretation")
    
    val = [id_value]
    # check if "Interpretation" is Yes
    if (row_values[85] == "Yes"):
        val.append("Interpretation")
        val = database_methods.fetch_values(86, 88, row_values, val)
        insert_helper.insert_row(val, "Translation_Interpretation")        
        
def insert_find_employment(row_values, id_value):
    '''
    Inserts data into the Find_Employment table.
    '''
    val = [id_value]
    # check if "Find employment" column is "Yes"
    if (row_values[33] == "Yes"):
        # get columns 34-38
        val = database_methods.fetch_values(34, 39, row_values, val)
        insert_helper.insert_row(val, "Find_Employment")

def insert_improve_skills(column_names, row_values, id_value):
    '''
    Inserts data into the Improve_Skills table.
    '''
    val = [id_value]
    if (type(row_values[29]) == str):
        val.append(column_names[29])
        val = database_methods.fetch_values(29, 30, row_values, val)
        insert_helper.insert_row(val, "Improve_Skills")
    
    val = [id_value]
    if (type(row_values[32]) == str):
        val.append(column_names[32])
        val = database_methods.fetch_values(32, 33, row_values, val)
        insert_helper.insert_row(val, "Improve_Skills")        

def insert_client_needs(column_values, row_values, id_value):
    '''
    Inserts data into the Client_Needs table. Values are all Yes/No
    '''
    # a list of (start, end) tuples for retrieving specifc columns
    insert_general.insert_3_value(column_values, row_values, 
                                  "Client_Needs", id_value, 11, 29)
    insert_general.insert_3_value(column_values, row_values, 
                                  "Client_Needs", id_value, 30, 32)   
    insert_general.insert_3_value(column_values, row_values, 
                                  "Client_Needs", id_value, 41, 47)  
    insert_general.insert_3_value(column_values, row_values, 
                                  "Client_Needs", id_value, 48, 68)
    
#if __name__ == "__main__":
    #df = pd.read_excel('file.xlsx')
    #column_values = df.iloc[1]
    #row_values = df.iloc[2]
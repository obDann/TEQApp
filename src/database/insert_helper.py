import sqlite3
import database_methods

def insert_row(lst, table):
    '''
    Inserts the values in lst into the database table.
    '''
    query = create_query(lst, table)
    database_methods.execute_query(query, lst, 'client_data.db')

def create_query(lst, table):
    '''
    Creates a query to insert values into the database.
    '''
    val = "("
    for i in range(0, len(lst) - 1):
        val = val + ("?, ")
    val = val + ("?);")
    return "INSERT INTO " + table + " values " + val   

import sys
sys.path.insert(0, "../database")
from database_methods import *

(conn, cur) = connection("client_data.db")

def find_years():
    '''
    Returns a list of years that clients attended a service
    '''
    lst = []
    query = "SELECT DISTINCT Year FROM Client_Attends_Service"
    
    cur.execute(query)
    rows = cur.fetchall()
    if (len(rows) > 0):
        for row in rows:
            lst.append(row[0])
    
    return lst
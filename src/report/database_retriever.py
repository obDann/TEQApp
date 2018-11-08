import sqlite3

def number_of_users(start_date, end_date):
    '''
    (str,str) -> 
    Given the time period (start and end date) return the number of
    users that are stored into the database within this period.
    '''
    conn = sqlite3.connect('client_data.db')
    cur = conn.cursor()
    
    cur.execute("SELECT COUNT(*),Unique_ID_Value FROM Client where")
    
    
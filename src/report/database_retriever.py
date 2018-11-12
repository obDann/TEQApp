import sqlite3

def number_of_users(start_date, end_date):
    conn = sqlite3.connect('client_data.db')
    cur = conn.cursor()
    
    cur.execute("SELECT COUNT(*),Unique_ID_Value FROM Client where")
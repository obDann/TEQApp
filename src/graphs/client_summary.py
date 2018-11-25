import sqlite3
from histogram import *
from pie_graph import *
from line_graph import *
import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.insert(0, "../database")
from database_methods import *

(conn, cur) = connection("client_data.db")

def client_language_pref():
    '''
    Displays client language perference.
    '''
    report_name = "Offical Language Preferences"
    x_axis = "Language Preference"
    y_axis = "People Count"  
    
    query = ("SELECT Official_Language_Preference ,COUNT(*) FROM Client "+
             "GROUP BY Client.Official_Language_Preference")

    cur.execute(query)
    result = cur.fetchall()
    
    if (result != []):
        df = pd.DataFrame(result)
        df.rename(columns={0: x_axis}, inplace=True);
        df.rename(columns={1: y_axis}, inplace=True);
    
        lang = list()
        for row in result:
            lang.append(row[0])
    
        # Graph
        p = PieGraph(df, x_axis, y_axis, report_name)
        p.display()

def phone_vs_email_usage():
    '''
    Displays a comparsion on how many clients uses phone, email, or both.
    '''
    report_name = "Phone Usage VS Email Usage for Clients"
    x_axis = "Ways to Contact"
    y_axis = "Usage"
    
    ways = ["Phone", "Email"]
    
    # Queries
    email_q = ("SELECT COUNT(*) FROM Client WHERE Client.Email > 0 AND "+ 
               "Client.Email_address IS NOT NULL")
    phone_q = ("SELECT COUNT(*) FROM Client WHERE Client.Phone > 0")
    
    cur.execute(email_q)
    email = cur.fetchall()
    
    cur.execute(phone_q)
    phone = cur.fetchall()
    
    if (email != [] and phone != []):
        list_count = list()
        list_count.append(phone[0])
        list_count.append(email[0])
        
        # Construct the dataframe
        ways = pd.DataFrame(ways,columns=[x_axis])
        count = pd.DataFrame(list_count,columns=[y_axis])
        df = pd.concat([ways, count],axis=1)
    
        hist = Histogram(df, x_axis, y_axis, report_name)
        hist.display(ways, 'bar')
    
def client_types(year, month):
    '''
    Given the year and the month, display the client count from each type.
    '''
    report_name = "Client Types"
    x_axis = "Agencies"
    y_axis = "Number of Clients"
    query = ("SELECT Client.Unique_ID_Type, COUNT(*) FROM Client WHERE "+ 
             "(strftime('%Y', Client.Processing_Details) = '"+ year +
             "' AND strftime('%m', Client.Processing_Details)  = '"+ month + "')" 
             " GROUP BY Client.Unique_ID_Type")
    
    cur.execute(query)
    result = cur.fetchall()
    if (result is not None or result != []):
        # Get the list of client types   
        types = list()
        for r in result:
            types.append(r[0])
        df = pd.DataFrame(result, columns=[x_axis, y_axis])
    
        # Graph
        hist = Histogram(df, x_axis, y_axis, report_name)
        hist.display(types, 'bar')
    
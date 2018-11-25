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

    df = pd.DataFrame(result)
    df.rename(columns={0: x_axis}, inplace=True);
    df.rename(columns={1: y_axis}, inplace=True);
    
    lang = list()
    for row in result:
        lang.append(row[0])
    
    # Graph
    #hist = Histogram(df, x_axis, y_axis, report_name)
    #hist.display(lang, 'bar')
    
def client_has_child():
    '''
    Displays how many child/children does clients have.
    '''
    report_name = "Number of Clients with Children"
    x_axis = "Number of Children"
    y_axis = "Client Count"  
    
    query = ("SELECT Official_Language_Preference ,COUNT(*) FROM Client "+
             "GROUP BY Client.Official_Language_Preference")

    cur.execute(query)
    result = cur.fetchall()
    pass

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
    
    # Make Dataframes
    p_df = pd.DataFrame(phone, columns=[ways[0]])
    e_df = pd.DataFrame(email, columns=[ways[1]])
    
    # Merge Dataframes
    df = pd.concat([p_df, e_df],axis=1)
    
    #hist = Histogram(df, x_axis, y_axis, report_name)
    #hist.display(ways, 'bar')
    
if __name__ == "__main__":
    #client_language_pref()
    #client_summary()
    #phone_vs_email_usage()
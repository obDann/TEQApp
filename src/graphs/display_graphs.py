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
total_clients = ("SELECT COUNT(*) FROM (SELECT DISTINCT " + 
                 "Client.Unique_ID_Value FROM Client)")
# Q2
def num_clients(year, service):
    '''
    Displays a line graph of how many times the given service us accessed in 
    each month of a given year.
    '''
    months = ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"]
    lst = []
    
    # set up dataframe
    for month in months:
        num_clients = ("SELECT COUNT(*) FROM Client, Client_Attends_Service, " 
                       + service + " WHERE Client.Unique_ID_Value = " + 
                       "Client_Attends_Service.Client_Unique_ID_Value AND " +
                       service + ".Service_ID = Client_Attends_" + 
                       "Service.Service_ID AND Client_Attends_Service.Month = '" 
                       + month + "' AND Client_Attends_Service.Year = '" 
                       + year + "'")
    
        cur.execute(num_clients)
        rows = cur.fetchall()
        total = rows[0][0]
        lst.append([month, total])
    
    df = pd.DataFrame(lst)
    df.rename(columns={0: 'Month', 1: 'Frequency'}, inplace=True);

    # display a line graph
    l = LineGraph(df, 'Month', 'Frequency', 'Number of Clients')
    l.display()
    

# Q3
def age_histogram(service):
    '''
    Displays a histogram of the ages of clients accessing a given service.
    '''
    age = ("SELECT (strftime('%Y', 'now') - strftime('%Y', Date_Of_Birth)) " +
             "- (strftime('%m-%d', 'now') < strftime('%m-%d', Date_Of_Birth)) " 
             + "FROM Client, Client_Attends_Service, " + service + " WHERE " 
             + "Client.Unique_ID_Value = Client_Attends_Service." + 
             "Client_Unique_ID_Value AND " + service + ".Service_ID " + 
             "= Client_Attends_Service.Service_ID")
    
    # set up the dataframe
    cur.execute(age)
    rows = cur.fetchall()
    lst = []
    for row in rows:
        lst.append(row[0])
    
    df = pd.DataFrame(lst)
    df.rename(columns={0: 'Age'}, inplace=True);
    bins = [0,10,20,30,40,50,60,70,80,90,100]

    # create the histogram
    hist = Histogram(df, 'Age', 'Frequency', 'Age of Clients in ' + service)
    hist.display(bins, 'bar')
    
    
def child_pie():
    lang_clients = ("SELECT COUNT(*) FROM (SELECT DISTINCT " + 
                    "Client.Unique_ID_Value FROM Client, Client_Enrolment"
                    + ", LT_Course WHERE LT_Course.Course_Code = " + 
                    "Client_Enrolment.Course_Code AND Client.Unique_ID_Value " 
                    + "= Client_Enrolment.Client_Unique_ID_Value)")    
    lst = []
    # set up dataframe
    cur.execute(lang_clients)
    rows = cur.fetchall()
    has_child = rows[0][0]
    lst.append(["Has Children", has_child])
    cur.execute(total_clients)
    rows = cur.fetchall()
    no_child = rows[0][0] - has_child
    lst.append(["No Children", no_child])
    df = pd.DataFrame(lst)
    df.rename(columns={0: 'Index', 1: 'Frequency'}, inplace=True);

    # create a pie graph
    p = PieGraph(df, 'Index', 'Frequency', 
                 "Clients in Language Training Courses")
    p.display()

def tran_pie():
    no_trans = ("SELECT COUNT(*) FROM (SELECT DISTINCT Client.Unique_ID_Value" 
                + " FROM Client, Client_Needs WHERE Client.Unique_ID_Value = " 
                + "Client_Needs.Client_Unique_ID_Value AND Client_Needs.Type = " 
                + " 'Transportation' AND Client_Needs.Value = 'No')")
    
    yes_trans = ("SELECT COUNT(*) FROM (SELECT DISTINCT Client.Unique_ID_Value" 
                 + " FROM Client, Client_Needs WHERE Client.Unique_ID_Value = " 
                 + "Client_Needs.Client_Unique_ID_Value AND " + 
                 "Client_Needs.Type = 'Transportation' AND " + 
                 "Client_Needs.Value = 'Yes')")    
    
    lst = []
    # set up dataframe
    cur.execute(no_trans)
    rows = cur.fetchall()
    no = rows[0][0]
    lst.append(["No Transportation", no])
    cur.execute(yes_trans)
    rows = cur.fetchall()
    yes = rows[0][0]
    lst.append(["Transportation", yes])
    df = pd.DataFrame(lst)
    df.rename(columns={0: 'Index', 1: 'Frequency'}, inplace=True);
    
    # create a pie graph
    p = PieGraph(df, 'Index', 'Frequency', "Clients Who Have Transportation")
    p.display()    

if __name__ == "__main__":
    #child_pie()
    #tran_pie()
    #age_histogram("Community_Connections")
    #num_clients("2018", "Community_Connections")
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

# Q1
def referral_age():
    report_name = "Number of Clients in Different Age Groups"
    # X axis
    label = "Age Groups"
    age_df = ["0-12","13-18","19-29","30-39","40-49","50-59","60-69",
              "70-79","80-89","90+"]
    age_df = pd.DataFrame(age_df, columns=[label])
    
    # Y axis
    frequency = "People Count"
    count_df = _get_age_groups()
    count_df = pd.DataFrame(count_df, columns=[frequency])
    
    # Merge the two columns
    df = pd.concat([age_df,count_df],axis=1)
    
    # Graph
    pie = PieGraph(df, label, frequency, report_name)
    pie.display()
    
def _get_age_groups():
    '''
    Gets the # of clients in each age group and store it into a list.
    '''
    age_query = ("SELECT (strftime('%Y', 'now') - " +
    "strftime('%Y', Client.Date_Of_Birth)) - (strftime('%m-%d', 'now') < "
    + "strftime('%m-%d', Client.Date_Of_Birth)) AS age from Client, Referral "
    +"WHERE Client.Unique_ID_Value = Referral.Client_Unique_ID_Value AND ")
    
    
    # Different age groups
    age_groups = list()
    age_groups.append("age > 0 AND age < 9")
    age_groups.append("age >10 AND age < 19")
    age_groups.append("age > 20 AND age < 29")
    age_groups.append("age > 30 AND age < 39")
    age_groups.append("age > 40 AND age < 49")
    age_groups.append("age > 50 AND age < 59")
    age_groups.append("age > 60 AND age < 69")
    age_groups.append("age > 70 AND age < 79")
    age_groups.append("age > 80 AND age < 89")
    age_groups.append("age > 90")
    
    client_count = list()

    for grp in age_groups:
        cur.execute(age_query+grp)
        result = cur.fetchall()
        client_count.append(len(result))
    
    return client_count

# Q2
def num_clients(year, service, name):
    '''
    Displays a line graph of how many times a client accessed a service in 
    each month of a given year.
    '''
    months = ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"]
    lst = []
    
    
    for month in months:
        # grab number of clients that attended that service for each month
        num_clients = ("SELECT COUNT(*) FROM Client, Client_Attends_Service, " 
                       + service + " WHERE Client.Unique_ID_Value = " + 
                       "Client_Attends_Service.Client_Unique_ID_Value AND " +
                       service + ".Service_ID = Client_Attends_" + 
                       "Service.Service_ID AND Client_Attends_Service.Month = '" 
                       + month + "' AND Client_Attends_Service.Year = '" 
                       + year + "'")
        
        # set up dataframe
        cur.execute(num_clients)
        rows = cur.fetchall()
        if (len(rows) > 0):
            total = rows[0][0]
            lst.append([month, total])
    
    df = pd.DataFrame(lst)
    df.rename(columns={0: 'Month', 1: 'Frequency'}, inplace=True);

    # display a line graph
    l = LineGraph(df, 'Month', 'Frequency', 'Number of Clients who attended ' 
                  + name + ' in ' + year)
    l.display()
    

# Q3
def age_histogram(service, name):
    '''
    Displays a histogram of the ages of clients accessing a given service.
    '''
    # grab all the ages of clients enrolled in the service
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
    if (len(rows) > 0):
        for row in rows:
            lst.append(row[0])
    
        df = pd.DataFrame(lst)
        df.rename(columns={0: 'Age'}, inplace=True);
        # bins for grouping the age
        bins = [0,10,20,30,40,50,60,70,80,90,100]

        # create the histogram
        hist = Histogram(df, 'Age', 'Frequency', 'Age of Clients in ' + name)
        hist.display(bins, 'bar')
    
    
def child_pie():
    '''
    Displays a pie graph that shows what percentage of clients enrolled in
    Language Traning Services have children.
    '''
    # grab number of clients who have children in language traning courses
    lang_clients = ("SELECT COUNT(*) FROM (SELECT DISTINCT " + 
                    "Client.Unique_ID_Value FROM Client, Client_Enrolment"
                    + ", LT_Course WHERE LT_Course.Course_Code = " + 
                    "Client_Enrolment.Course_Code AND Client.Unique_ID_Value " 
                    + "= Client_Enrolment.Client_Unique_ID_Value)")    
    # set up dataframe
    lst = []
    cur.execute(lang_clients)
    rows = cur.fetchall()
    if (len(rows) > 0):
        has_child = rows[0][0]
    else:
        has_child = 0
    lst.append(["Has Children", has_child])
    cur.execute(total_clients)
    rows = cur.fetchall()
    if (len(rows) > 0):
        no_child = rows[0][0] - has_child
    else:
        no_child = 0
    lst.append(["No Children", no_child])
    df = pd.DataFrame(lst)
    df.rename(columns={0: 'Index', 1: 'Frequency'}, inplace=True);

    # create a pie graph
    p = PieGraph(df, 'Index', 'Frequency', 
                 "Clients in Language Training Courses")
    p.display()

def tran_pie():
    '''
    Displays a pie graph showing the percentage of clients who have access
    to transportation.
    '''
    # grab number of clients that have no transportation
    no_trans = ("SELECT COUNT(*) FROM (SELECT DISTINCT Client.Unique_ID_Value" 
                + " FROM Client, Client_Needs WHERE Client.Unique_ID_Value = " 
                + "Client_Needs.Client_Unique_ID_Value AND Client_Needs.Type = " 
                + " 'Transportation' AND Client_Needs.Value = 'No')")
    
    # grab number of clients that have transportation
    yes_trans = ("SELECT COUNT(*) FROM (SELECT DISTINCT Client.Unique_ID_Value" 
                 + " FROM Client, Client_Needs WHERE Client.Unique_ID_Value = " 
                 + "Client_Needs.Client_Unique_ID_Value AND " + 
                 "Client_Needs.Type = 'Transportation' AND " + 
                 "Client_Needs.Value = 'Yes')")    
    
    # set up dataframe
    lst = []
    cur.execute(no_trans)
    rows = cur.fetchall()
    if (len(rows) > 0):
        no = rows[0][0]
    else:
        no = 0
    lst.append(["No Transportation", no])
    cur.execute(yes_trans)
    rows = cur.fetchall()
    if (len(rows) > 0):
        yes = rows[0][0]
    else:
        yes = 0
    lst.append(["Transportation", yes])
    df = pd.DataFrame(lst)
    df.rename(columns={0: 'Index', 1: 'Frequency'}, inplace=True);
    
    # create a pie graph
    p = PieGraph(df, 'Index', 'Frequency', "Clients Who Have Transportation")
    p.display()
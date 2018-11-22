import sqlite3

conn = sqlite3.connect('client_data.db')
cur = conn.cursor()

# Getting the age of the client
age_query = ("SELECT (strftime('%Y', 'now') - strftime('%Y', Client.Date_Of_Birth)) - (strftime('%m-%d', 'now') < strftime('%m-%d', Client.Date_Of_Birth)) from Client")

# Q1
# Gets the # of people who asked for a referral to some service
query1 = ("SELECT COUNT(*) FROM Client, Referral WHERE "+
          "Client.Unique_ID_value = Referral.Client_Unique_ID_value")

# Gets the # of people who has a referral for find employement
query2 = ("SELECT COUNT(*) FROM Client, Referral, Find_Employment WHERE "+
          "Client.Unique_ID_value = Find_Employment.Client_Unique_ID_value")

# Gets the # of people who has a referral for skill improvement
query3 = ("SELECT COUNT(*),Improve FROM Client,Improve_Skills WHERE "+
          "Client.Unique_ID_value = Improve_Skills.Client_Unique_ID_value")

# Gets the # of people who has a referral for client Needs
query4 = ("SELECT COUNT(*),Type FROM Client, Referral, Client_Needs WHERE "+
          "Client.Unique_ID_value = Client_Needs.Client_Unique_ID_value")

# Getting the # of people who needs a translation service
query5 = ("SELECT COUNT(*),Type FROM Client,Translation_Interpretation WHERE "+
          "Client.Unique_ID_value = "+
          "Translation_Interpretation.Client_Unique_ID_value")

# Getting the # of people who wants to become a canadian citizen
query6 = ("SELECT COUNT(*) FROM Referral WHERE "+
          "Referral.Canadian_Citizen_Intention = 'Y'")
# Getting the # of people who does not wants to become a canadian citizen
query7 = ("SELECT COUNT(*) FROM Referral WHERE "+
          "Referral.Canadian_Citizen_Intention = 'N'")

# Getting the # of people who received their support service
query8 = ("SELECT COUNT(*) FROM Referral WHERE "+
          "Referral.Support_Services_Received  = 'Y'")
# Getting the # of people who did not receive support service
query9 = ("SELECT COUNT(*) FROM Referral WHERE "+
          "Referral.Support_Services_Received  = 'N'")

# Getting the # of people who required their support service
query10 = ("SELECT COUNT(*) FROM Referral WHERE "+
          "Referral.Suport_Services_Required  = 'Y'")
# Getting the # of people who does not require support service
query11 = ("SELECT COUNT(*) FROM Referral WHERE "+
          "Referral.Suport_Services_Required  = 'N'")

# Getting the # of people who has their settlement plan completed
query12 = ("SELECT COUNT(*) FORM Referral WHERE "+
          "Referral.Settlement_Plan_Completed = 'Y'")
# Getting the # of people who does not have their settlement plan completed
query13 = ("SELECT COUNT(*) FORM Referral WHERE "+
          "Referral.Settlement_Plan_Completed = 'N'")

# Getting the # of people who needs Non IRCC Services
query14 = ("SELECT COUNT(*) FORM Referral WHERE "+
          "Referral.Non_IRCC_Services = 'Y'")
# Getting the # of people who doesnt need Non IRCC Services
query15 = ("SELECT COUNT(*) FORM Referral WHERE "+
          "Referral.Non_IRCC_Services = 'N'")

cur.execute(query1)
rows = cur.fetchall()
for r in rows:
    print(r)
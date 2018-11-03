import sqlite3
import database_methods

def insert_user(username, name, password, account_type):
    '''
    Inserts a new user into the database (table User).
    '''
    # time is stored as UNIX timestap in INT
    query = "INSERT INTO User values (?, ?, ?, ?, strftime('%s','now'));"
    fields = (username, name, password, account_type)
    
    if (not(database_methods.execute_query(query, fields, 'users.db'))):
        insert_account(username, account_type)

def insert_account(username, account_type):
    if (account_type == "Agency"):
        status = "Active"
        query = "INSERT INTO Agency_User values (?, ?)"
        fields = (username, status)
        database_methods.execute_query(query, fields, 'users.db')
        
def login(username, password):
    '''
    Returns the name of the user and the type if login information is correct.
    '''
    (conn, cur) = database_methods.connection('users.db')
    query = ("SELECT Name, Type from User where Username = ? "
            " AND password = ?")
    fields = (username, password)
    try:
        cur.execute(query, fields)
        error = 0
    except sqlite3.Error as e:
        print(format(e))
        error = 1
    
    if (not(error)):
        name = cur.fetchall()
        if (name[0][0] is not None):
            return (name[0][0], name[0][1])
        
    return (None, None)

def insert_file_info(num, username, filename, service, month, year):
    '''
    Inserts a record of a file submission into the database.
    '''
    query = ("INSERT INTO Submission_History "
            + "values (?, ?, ?, ?, ?, ?, strftime('%s','now'))")
    fields = (num, username, filename, service, month, year)
    database_methods.execute_query(query, fields, 'users.db')
    
def insert_request(num, username, desc):
    '''
    Insert a request from the TEQ staff into table Request.
    '''
    status = "Pending"
    query = ("INSERT INTO Request (ID, Username, Description, Status, "
             "Date_Submitted) values (?, ?, ?, ?, strftime('%s','now'))")
    fields = (num, username, desc, status)
    database_methods.execute_query(query, fields, 'users.db')

def accepted_request(num, username):
    '''
    An admin accepted a request for change in data fields.
    '''
    status = "Accepted"
    query = ("UPDATE Request SET Admin_Username = ?, Status = ?, "
             "Date_Accepted = strftime('%s','now') WHERE ID = ?")
    fields = (username, status, num)
    database_methods.execute_query(query, fields, 'users.db')

def update_agency_status(username, status):
    '''
    Update an agency's status.
    '''
    query = "Update Agency_User SET Status = ? WHERE Username = ?"
    fields = (status, username)
    database_methods.execute_query(query, fields, 'users.db')
    
def get_tables_names():
    '''
    A function which gets all the table names of a database.
    Returns a list of table names.
    '''
    (conn, curr) = connection() 
    curr.execute("SELECT name FROM sqlite_master WHERE type='table';")
    result = [row[0] for row in curr.fetchall()]
    return result

if __name__ == "__main__":
    insert_user("xyz", "sam", "sam123", "Agency")
    insert_user("mike22", "Mike", "mike123", "TEQ")
    insert_user("bobbob", "Bob", "bob123", "Admin")
    insert_file_info('1', 'xyz', 'file.xlsx', 'Employment', 'April', '2010')
    # mike requests a deletion
    insert_request('1', 'mike22', 'Delete field Child1')
    # bob accepts the request
    accepted_request('1', 'bobbob')
    # changed xyzs status to Inactive
    update_agency_status("xyz", "Inactive")
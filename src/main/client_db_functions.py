import sqlite3

def connection():
    try:
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
    except sqlite3.Error as e:
        print(format(e))
        
    return (conn, cur)

def check_connection():
    (conn, cur) = connection()
    if (conn is not None and cur is not None):
        return True
    
    return False

def execute_query(query, fields):
    error = 1
    if (check_connection()):
        (conn, cur) = connection()
        try:
            cur.execute(query, fields)
            conn.commit()
            error = 0
        except sqlite3.Error as e:
            print(e)
            conn.rollback()
    
    return error

def insert_user(username, name, password, account_type):
    '''
    Inserts a new user into the database (table User).
    '''
    # time is stored as UNIX timestap in INT
    query = "INSERT INTO User values (?, ?, ?, ?, strftime('%s','now'));"
    fields = (username, name, password, account_type)
    
    if (not(execute_query(query, fields))):
        insert_account(username, account_type)

def insert_account(username, account_type):
    if (account_type == "Agency"):
        status = "Active"
        query = "INSERT INTO Agency_User values (?, ?)"
        fields = (username, status)
        execute_query(query, fields)
        
def login(username, password):
    '''
    Returns the name of the user and the type if login information is correct.
    '''
    (conn, cur) = connection()
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
    execute_query(query, fields)
    
def insert_request(num, username, desc):
    '''
    Insert a request from the TEQ staff into table Request.
    '''
    status = "Pending"
    query = ("INSERT INTO Request (ID, Username, Description, Status, "
             "Date_Submitted) values (?, ?, ?, ?, strftime('%s','now'))")
    fields = (num, username, desc, status)
    execute_query(query, fields)

def accepted_request(num, username):
    '''
    An admin accepted a request for change in data fields.
    '''
    status = "Accepted"
    query = ("UPDATE Request SET Admin_Username = ?, Status = ?, "
             "Date_Accepted = strftime('%s','now') WHERE ID = ?")
    fields = (username, status, num)
    execute_query(query, fields)

def update_agency_status(username, status):
    '''
    Update an agency's status.
    '''
    query = "Update Agency_User SET Status = ? WHERE Username = ?"
    fields = (status, username)
    execute_query(query, fields)
    
def get_tables_names():
        '''
        A function which gets all the table names of a database.
        Returns a list of table names.
        '''
        table_names = list()
        conn = sqlite3.connect('test.db')
        cur = conn.cursor()     
        cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        result = cur.fetchall()
        for table in result:
                print(table[0])
                table_names.append(table)
        conn.close()
        return table_names

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
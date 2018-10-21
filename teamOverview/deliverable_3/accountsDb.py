from datetime import date, datetime
import mysql.connector
    
def connection():
    try:
        cnx = mysql.connector.connect(user='root', password='yourpassword',
                                  host='127.0.0.1',
                                  database='users')
        cursor = cnx.cursor()
        error = 0
    except mysql.connector.Error as err:
        print(format(err))
        error = 1
    
    if (not(error)):
        return (cnx, cursor)
    return (None, None)

def check_connection():
    (cnx, cursor) = connection()
    if (cnx is not None and cursor is not None):
        return True
    
    return False
    
def execute_query(query, fields):
    error = 1
    if (check_connection()):
        (cnx, cursor) = connection()
        try:
            cursor.execute(query, fields)
            cnx.commit()
            error = 0
        except mysql.connector.Error as err:
            print(err)
            cnx.rollback()
    
    return error

def insert_user(username, name, password, account_type):
    '''
    Inserts a new user into the database (table User).
    '''
    date = datetime.now()
    # password stored using SHA1 algorithm in mysql
    query = "INSERT INTO User values (%s, %s, SHA1(%s), %s, %s)"
    fields = (username, name, password, account_type, date)
    
    if (not(execute_query(query, fields))):
        insert_account(username, account_type)

# Currently database only has an Agency accounts table
# may add a TEQ staff and admin table in the future
def insert_account(username, account_type):
    if (account_type == "Agency"):
        status = "Active"
        query = "INSERT INTO Agency_User values (%s, %s)"
        fields = (username, status)
        execute_query(query, fields)

def login(username, password):
    '''
    Returns the name of the user if login information is correct.
    '''
    (cnx, cursor) = connection()
    query = ("SELECT Name from User where Username = %s "
            " AND password = SHA1(%s)")
    fields = (username, password)
    try:
        cursor.execute(query, fields)
        error = 0
    except mysql.connector.Error as err:
        print(err)
        error = 1
    
    if (not(error)):
        name = cursor.fetchone()
        if (name is not None):
            return name[0]
        
    return None

def insert_file_info(num, username, filename, service, month, year):
    '''
    Inserts a record of a file submission into the database.
    '''
    date = datetime.now()
    query = "INSERT INTO Submission_History values (%s, %s, %s, %s, %s, %s, %s)"
    fields = (num, username, filename, service, month, year, date)
    execute_query(query, fields)
    
def insert_request(num, username, desc):
    '''
    Insert a request from the TEQ staff into table Request.
    '''
    date = datetime.now()
    status = "Pending"
    query = ("INSERT INTO Request (ID, Username, Description, Status, "
             "Date_Submitted) values (%s, %s, %s, %s, %s)")
    fields = (num, username, desc, status, date)
    execute_query(query, fields)

def accepted_request(num, username):
    '''
    An admin accepted a request for change in data fields.
    '''
    date = datetime.now()
    status = "Accepted"
    query = ("UPDATE Request SET Admin_Username = %s, Status = %s, "
             "Date_Accepted = %s WHERE ID = %s")
    fields = (username, status, date, num)
    execute_query(query, fields)

def update_agency_status(username, status):
    '''
    Update an agency's status.
    '''
    query = "Update Agency_User SET Status = %s WHERE Username = %s"
    fields = (status, username)
    execute_query(query, fields)
    
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

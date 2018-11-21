import sqlite3

def connection(database):
    '''
    Creates a connection to the database.
    '''
    try:
        conn = sqlite3.connect(database)
        cur = conn.cursor()
        # enable foreign key constraint
        cur.execute("PRAGMA foreign_keys = ON")
    except sqlite3.Error as e:
        print(format(e))
        
    return (conn, cur)

def execute_query(query, fields, database):
    '''
    Executes a SQL command using the query and fields.
    '''
    error = 1
    (conn, cur) = connection(database)
    try:
        cur.execute(query, fields)
        conn.commit()
        error = 0
    except sqlite3.Error as e:
        print(e)
        conn.rollback()
    
    return error 
    
def get_id(table):
    '''
    Gets maximum ID in the table.
    '''
    (conn, cur) = connection('client_data.db')
    query = ("select max(ID) from " + table)
    try:
        cur.execute(query)
        error = 0
    except sqlite3.Error as e:
        print(format(e))
        error = 1
    
    if (not(error)):
        val = cur.fetchone()
        if (val is not None and val[0] is not None):
            return val[0]
        else:
            return 0


def check_id(client_id, database, table, id_name):
    '''
    Checks if there is a row for the client with client_id. Returns 1 if yes
    and 0 otherwise.
    '''
    query = ("SELECT 1 FROM " + str(table) + " WHERE " + str(id_name) + " = " 
             + str(client_id))
    
    (conn, cur) = connection(database)
    try:
        error = 0
        cur.execute(query)
    except sqlite3.Error as e:
        print(e)
        error = 1
    
    if (not(error)):
        val = cur.fetchone()
        if (val is not None and val[0] == 1):
            return 1
        else:
            return 0

def check_course(course_code, database):
    query = ("SELECT 1 FROM " + "LT_Course" + " WHERE " +
             "Course_Code" + " = " + "'" + str(course_code) + "'")
    
    (conn, cur) = connection(database)
    try:
        error = 0
        cur.execute(query)
    except sqlite3.Error as e:
        print(e)
        error = 1
    
    if (not(error)):
        val = cur.fetchone()
        if (val is not None and val[0] == 1):
            return 1
        else:
            return 0    

def fetch_values(start, end, row_values, lst):
    '''
    Returns a list of the values extracted from a row in the excel file.
    '''
    i = start
    ret = lst
    while (i < end):
        value = row_values[i]
        ret.append(value)
        i += 1
    
    return ret

# General method for inserting with a list of indices
def fetch_values_list(row_values, index_list, val):
    i = 0
    while (i < len(index_list)):
        start = index_list[i][0]
        end = index_list[i][1]
        while (start < end):
            val.append(row_values[start])
            start += 1
        i += 1
    
    return val

def update_lists(lst, column_values, row_values, index_list):
    '''
    Returns a list of columns that need to be updated.
    '''
    i = 0
    j = 0
    col = []
    data = []
    if (lst is not None):
        column = lst
    else:
        column = column_values

    while (i < len(index_list)):
        start = index_list[i][0]
        end = index_list[i][1]
        while (start < end):
            if (type(row_values[start]) == str):
                col.append(column[j])
                data.append(row_values[start])
            start += 1
            j += 1
        i += 1
    return (col, data)

def get_existing_id(database, table, column, prim_key, value):
    '''
    Returns the current id value of a specific column specified by the
    table and primary key value.
    '''
    query = ("SELECT " + column + " FROM " + table + " WHERE " + prim_key +
            " = " + value)
    
    (conn, cur) = connection(database)
    try:
        error = 0
        cur.execute(query)
    except sqlite3.Error as e:
        print(e)
        error = 1
    
    if (not(error)):
        val = cur.fetchone()
        if (val is not None and val[0] is not None):
            return val[0]
        else:
            return None

def create_update_query(column_values, data, table, prim_key, id_val):
    '''
    Creates a query to update data in the database for a client.
    '''
    set_body = "SET "
    i = 0
    while (i < len(column_values)):
        cond = str(column_values[i]) + " = '" + str(data[i]) + "', "
        set_body += cond
        i += 1
    query = ("UPDATE " + table + " " + set_body[:len(set_body) - 2] + " WHERE " 
            + prim_key + " = " + str(id_val))
    
    return query

def update_query(query, database):
    error = 1
    (conn, cur) = connection(database)
    try:
        cur.execute(query)
        conn.commit()
        error = 0
    except sqlite3.Error as e:
        print(e)
        conn.rollback()
    
    return error 
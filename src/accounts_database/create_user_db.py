import sqlite3


def create_tables():
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()

    cur.execute("PRAGMA foreign_keys = ON")

    cur.execute("""CREATE TABLE IF NOT EXISTS User (
            Username text PRIMARY KEY NOT NULL,
            Email text NOT NULL UNIQUE,
            Name text NOT NULL,
            Password text NOT NULL,
            Type text NOT NULL,
            Date_Created INT NOT NULL);""")

    cur.execute("""CREATE TABLE IF NOT EXISTS Agency_User (
            Username text PRIMARY KEY NOT NULL,
            Status text NOT NULL,
            FOREIGN KEY (Username) references User(Username));""")

    cur.execute("""CREATE TABLE IF NOT EXISTS Submission_History (
            ID INT PRIMARY KEY NOT NULL,
            Username text NOT NULL,
            Name text NOT NULL,
            Type text NOT NULL,
            Month_File text NOT NULL,
            Year_File INT NOT NULL,
            Date_Submitted INT NOT NULL,
            FOREIGN KEY (Username) references User(Username));""")

    cur.execute("""CREATE TABLE IF NOT EXISTS Request (
            ID INT PRIMARY KEY NOT NULL,
            Username text NOT NULL,
            Admin_Username text,
            Description text NOT NULL,
            Status text NOT NULL,
            Date_Submitted INT NOT NULL,
            Date_Accepted INT,
            FOREIGN KEY (Username) references User(Username),
            FOREIGN KEY (Admin_Username) references User(Username));""")

    cur.execute("""CREATE TABLE IF NOT EXISTS Temp_Passcode (
            Username text PRIMARY KEY NOT NULL,
            Temp_Pass text NOT NULL);""")

    conn.close()

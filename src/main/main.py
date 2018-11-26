import tkinter as tk
from tkinter import *
import console
import create_user_db
sys.path.insert(0, "../database")
import create_data_db

def run():
    # Create database for user accounts
    create_user_db.create_tables()
    
    # Create database for client data
    create_data_db.create_tables()
    
    # Run console
    app = console.TeqApp()
    app.geometry('800x650')
    app.title("TEQLIP Application")
    app.mainloop()

if __name__ == "__main__":
    run()
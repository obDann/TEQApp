import tkinter as tk
from tkinter import *
import console
import create_user_db

def run():
    # Create database for user accounts
    create_user_db.create_tables()
    
    # Run console
    app = console.TeqApp()
    app.geometry('800x600')
    app.title("TEQLIP Application")
    app.mainloop()

if __name__ == "__main__":
    run()
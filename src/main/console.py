import tkinter as tk
from tkinter import *
import client_db_functions
from main_page import *
from login_page import *
from create_account_page import *
from agency_page import *
from teq_page import *
from admin_page import *
from file_upload_page import *

#from https://pythonprogramming.net/change-show-new-frame-tkinter/
#for class structure and init arguments
class TeqApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        self.cont = tk.Frame(self)

        self.cont.pack(side="top", fill="both", expand = True)

        self.cont.grid_rowconfigure(0, weight=1)
        self.cont.grid_columnconfigure(0, weight=1)

        self.display(MainPage)

    def display(self, page):
        frame = page(self.cont, self)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()
        
    def set_page(self, f, name):
        frame = f(self.cont, self, name)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

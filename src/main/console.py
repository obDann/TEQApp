import tkinter as tk
from tkinter import *
sys.path.insert(0, "../accounts_database")
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
        '''
        (TeqApp, *args, **kwargs) -> None

        Initializes the TEQ application
        '''
        # make the root
        tk.Tk.__init__(self, *args, **kwargs)
        self.cont = tk.Frame(self)
        self.cont.pack(side="top", fill="both", expand = True)

        self.cont.grid_rowconfigure(0, weight=1)
        self.cont.grid_columnconfigure(0, weight=1)
        # go to the main page on initialization
        self.display(MainPage)

    def display(self, page):
        '''
        (TeqApp, Frame) -> None

        Goes to another page without providing anything
        '''
        frame = page(self.cont, self)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

    def set_page(self, f, name):
        '''
        (TeqApp, Frame, str) -> None

        Goes to another page while providing a specific name
        '''
        frame = f(self.cont, self, name)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

    def insert_page_details(self, page, df, template_name):
        '''
        (TeqApp, Frame, DataFrame, str) -> None

        Goes to another page while providing a dataframe and a template name
        '''
        my_frame = page(self.cont, self, df, template_name)
        # set the grid
        my_frame.grid(row=0, column=0, sticky="nsew")
        # go to page
        my_frame.tkraise()

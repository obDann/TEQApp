import tkinter as tk
from tkinter import *
from console import *
import main_page as mp
from create_account_page import *
from agency_page import *
from teq_page import *
from admin_page import *
from file_upload_page import *

class LoginPage(tk.Frame):

    def __init__(self, parent, controller):
        self.cont = controller
        tk.Frame.__init__(self, parent)

        Label(self, text="Username").grid(row=1)
        Label(self, text="Password").grid(row=2)

        self.e1 = Entry(self)
        self.e1.grid(row=1, column=1)
        self.e2 = Entry(self, show="*")
        self.e2.grid(row=2, column=1)

        b1 = Button(self, text="Back",
                    command=lambda: self.cont.display(mp.MainPage))
        b1.grid(row=5, column=1, sticky=W, pady=6)

        b2 = Button(self, text="Login", command=self.log_user)
        b2.grid(row=5, column=2, sticky=W, pady=6)

    def log_user(self):
        username = self.e1.get()
        pw = self.e2.get()

        if (username != "" and pw != ""):
            # grab name and type of acc if login was successful
            (name, acc) = client_db_functions.login(username, pw)
            if (name != None and acc != None):
                self.check_type(name, acc)

    def check_type(self, name, acc):
        if (acc == "Agency"):
            self.cont.set_page(AgencyPage, name)
        elif (acc == "TEQ"):
            self.cont.set_page(TEQPage, name)
        else:
            self.cont.set_page(AdminPage, name)

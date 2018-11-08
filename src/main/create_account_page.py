import tkinter as tk
from tkinter import *
from console import *
import main_page as mp
from login_page import *
from agency_page import *
from teq_page import *
from admin_page import *
from file_upload_page import *

class CreateAccountPage(tk.Frame):

    def __init__(self, parent, controller):
        self.cont = controller
        tk.Frame.__init__(self, parent)

        Label(self, text="Username").grid(row=1)
        Label(self, text="First Name").grid(row=2)
        Label(self, text="Password").grid(row=3)
        Label(self, text="Choose an Account").grid(row=4)

        self.e1 = Entry(self)
        self.e1.grid(row=1, column=1)
        self.e2 = Entry(self)
        self.e2.grid(row=2, column=1)
        self.e3 = Entry(self, show="*")
        self.e3.grid(row=3, column=1)

        # Options menu for selecting which account
        self.acc = StringVar(self)
        choice = {"Agency", "TEQ", "Admin"}
        self.acc.set("Agency")
        menu = OptionMenu(self, self.acc, *choice)
        menu.grid(row=4, column=1)

        b1 = Button(self, text="Back",
                            command=lambda: self.cont.display(mp.MainPage))
        b1.grid(row=5, column=1, sticky=W, pady=6)

        b2 = Button(self, text="Submit", command=self.create_user)
        b2.grid(row=5, column=2, sticky=W, pady=6)

    def create_user(self):
        username = self.e1.get()
        name = self.e2.get()
        pw = self.e3.get()
        acc = self.acc.get()

        if (username != "" and name != "" and pw != ""):
            client_db_functions.insert_user(username, name, pw, acc)
            self.cont.display(mp.MainPage)
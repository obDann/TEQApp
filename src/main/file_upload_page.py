import tkinter as tk
from tkinter import *
import client_db_functions
from console import *
from main_page import *
from login_page import *
from create_account_page import *
import agency_page as ap
from teq_page import *
from admin_page import *

class FileUpload(tk.Frame):

    def __init__(self, parent, controller, name):
        self.cont = controller
        self.name = name
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Choose a type to upload:")
        label.pack(side=TOP,fill=X)

        #Buttons dont work
        b1 = tk.Button(self, text="Client Profile")
        b1.pack(side=TOP,fill=X)

        b2 = tk.Button(self, text="Needs Assessment & Referrals")
        b2.pack(side=TOP,fill=X)

        b3 = tk.Button(self, text="Community Connections")
        b3.pack(side=TOP,fill=X)

        b4 = tk.Button(self, text="Information and Orientation")
        b4.pack(side=TOP,fill=X)

        b5 = tk.Button(self, text="Employment Related Services")
        b5.pack(side=TOP,fill=X)

        b6 = tk.Button(self, text="Language Training - Client Enrol")
        b6.pack(side=TOP,fill=X)

        b7 = tk.Button(self, text="Language Training - Course Setup")
        b7.pack(side=TOP,fill=X)

        b8 = tk.Button(self, text="Language Training - Client Exit")
        b8.pack(side=TOP,fill=X)

        back = Button(self, text="Back",
                            command=self.back)
        back.pack(side=TOP,fill=X)

    def back(self):
        self.cont.set_page(ap.AgencyPage, self.name)
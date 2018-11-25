import tkinter as tk
from tkinter import *
from console import *
from login_page import *
from create_account_page import *
from agency_page import *
from teq_page import *
from file_upload_page import *

class MainPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Please choose one of the following:")
        label.pack(side=TOP,fill=X)

        b1 = tk.Button(self, text="Login",
                       command=lambda: controller.display(LoginPage))
        b1.pack(side=TOP,fill=X)

        b2 = tk.Button(self, text="Create a New Account",
                       command=lambda: controller.display(CreateAccountPage))
        b2.pack(side=TOP,fill=X)

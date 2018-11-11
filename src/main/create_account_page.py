import tkinter as tk
from tkinter import *
from console import *
import main_page as mp
from login_page import *
from agency_page import *
from teq_page import *
from admin_page import *
from file_upload_page import *
from button_observable import *
from create_user_observer import *

class CreateAccountPage(tk.Frame):

    def __init__(self, parent, controller):
        self.cont = controller
        tk.Frame.__init__(self, parent)

        Label(self, text="Username").grid(row=1)
        Label(self, text="First Name").grid(row=2)
        Label(self, text="Password").grid(row=3)
        Label(self, text="Choose an Account").grid(row=4)

        obs_button = ButtonObservable()
        obs_button.set_button(Button(self, text="Submit", command=lambda: obs_button.raise_event(self)))
        cuo = CreateUserObserver()
        obs_button.add_observer(cuo)
        b2 = obs_button.button
        b2.grid(row=5, column=2, sticky=W, pady=6)

        b2.e1 = Entry(self)
        b2.e1.grid(row=1, column=1)
        b2.e2 = Entry(self)
        b2.e2.grid(row=2, column=1)
        b2.e3 = Entry(self, show="*")
        b2.e3.grid(row=3, column=1)

        # Options menu for selecting which account
        b2.acc = StringVar(self)
        choice = {"Agency", "TEQ", "Admin"}
        b2.acc.set("Agency")
        menu = OptionMenu(self, b2.acc, *choice)
        menu.grid(row=4, column=1)

        b1 = Button(self, text="Back",
                            command=lambda: self.cont.display(mp.MainPage))
        b1.grid(row=5, column=1, sticky=W, pady=6)

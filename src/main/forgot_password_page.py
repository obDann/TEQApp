import tkinter as tk
from tkinter import *
from console import *
import main_page as mp
from login_page import *
from create_account_page import *
from agency_page import *
from teq_page import *
from file_upload_page import *
from button_observable import *
from email_observer import *


class ForgotPasswordPage(tk.Frame):

    def __init__(self, parent, controller):
        self.cont = controller
        tk.Frame.__init__(self, parent)

        Label(self, text="Enter your Email:").grid(row=1, column=1)

        obs_button = ButtonObservable()
        obs_button.set_button(Button(self, text="Send",
                                     command=lambda: obs_button.raise_event(self)))
        email_obs = EmailObserver()
        obs_button.add_observer(email_obs)
        b2 = obs_button.button
        b2.grid(row=3, column=2, sticky=W, pady=6)

        b2.e1 = Entry(self)
        b2.e1.grid(row=2, column=1)

        b1 = Button(self, text="Back",
                    command=lambda: self.cont.display(mp.LoginPage))
        b1.grid(row=3, column=1, sticky=W, pady=6)

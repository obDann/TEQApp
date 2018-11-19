import tkinter as tk
from tkinter import *
from console import *
import main_page as mp
from create_account_page import *
from agency_page import *
from teq_page import *
from admin_page import *
from file_upload_page import *
from button_observable import *
from login_observer import *
from change_password_observer import *


class ChangePasswordPage(tk.Frame):

    def __init__(self, parent, controller, username):
        self.cont = controller
        tk.Frame.__init__(self, parent)

        Label(self, text="Enter a new password:").grid(row=1, column=1)
        Label(self, text="Confirm your password:").grid(row=3, column=1)
        Label(self,
              text="Note: make sure the passwords match.").grid(row=5,column=1)

        obs_button = ButtonObservable()
        obs_button.set_button(Button(self, text="Confirm",
                                     command=lambda: obs_button.raise_event(self)))
        changepw_obs = ChangePasswordObserver()
        obs_button.add_observer(changepw_obs)
        b2 = obs_button.button
        b2.grid(row=6, column=2, sticky=W, pady=6)
        b2.user = username
        b2.e1 = Entry(self, show="*")
        b2.e1.grid(row=2, column=1)
        b2.e2 = Entry(self, show="*")
        b2.e2.grid(row=4, column=1)

        b1 = Button(self, text="Back",
                    command=lambda: self.cont.display(mp.LoginPage))
        b1.grid(row=6, column=1, sticky=W, pady=6)

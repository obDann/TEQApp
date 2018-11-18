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
from forgot_password_page import *


class LoginPage(tk.Frame):

    def __init__(self, parent, controller):
        self.cont = controller
        tk.Frame.__init__(self, parent)

        Label(self, text="Username").grid(row=1)
        Label(self, text="Password").grid(row=2)

        obs_button = ButtonObservable()
        obs_button.set_button(Button(self, text="Login",
                                     command=lambda: obs_button.raise_event(self)))
        log_obs = LoginObserver()
        obs_button.add_observer(log_obs)
        b2 = obs_button.button
        b2.grid(row=5, column=2, sticky=W, pady=6)

        b2.e1 = Entry(self)
        b2.e1.grid(row=1, column=1)
        b2.e2 = Entry(self, show="*")
        b2.e2.grid(row=2, column=1)

        b1 = Button(self, text="Back",
                    command=lambda: self.cont.display(mp.MainPage))
        b1.grid(row=6, column=1, sticky=W, pady=6)

        b3 = Button(self, text="Forgot Password?",
                    command=lambda: self.cont.display(ForgotPasswordPage))
        b3.grid(row=5, column=1, sticky=W, pady=6)

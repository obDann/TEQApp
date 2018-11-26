import tkinter as tk
from tkinter import *
from console import *
import teq_page as tq
from login_page import *
from agency_page import *
from teq_page import *
from file_upload_page import *
from button_observable import *
from create_user_observer import *
from delete_account_observer import *

class DeleteAccountPage(tk.Frame):

    def __init__(self, parent, controller, name):
        self.cont = controller
        tk.Frame.__init__(self, parent)

        Label(self, text="Username of account:").grid(row=1, column=1)

        # create an observable button
        obs_button = ButtonObservable()
        my_butt = Button(self,
                         text="Delete",
                         command=lambda: obs_button.raise_event(self))
        obs_button.set_button(my_butt)
        create_usr_obs = DeleteAccountObserver()
        obs_button.add_observer(create_usr_obs)
        b2 = obs_button.button
        b2.grid(row=3, column=2, sticky=W, pady=6)

        # set entrys for the observable button
        b2.e1 = Entry(self)
        b2.e1.grid(row=2, column=1)

        b1 = Button(self, text="Back",
                    command=lambda: self.cont.set_page(tq.TEQPage, name))
        b1.grid(row=3, column=1, sticky=W, pady=6)

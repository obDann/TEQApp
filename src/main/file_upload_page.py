import tkinter as tk
from tkinter import *
import client_db_functions
from console import *
from main_page import *
from login_page import *
from create_account_page import *
import agency_page as ap
from teq_page import *
from upload_observer import *
from button_observable import *

'''
Import commands
'''
sys.path.insert(0, "../commands")
from file_system_fetcher import *


class FileUpload(tk.Frame):

    def __init__(self, parent, controller, name):
        self.cont = controller
        self.name = name
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Choose a type to upload:")
        label.pack(side=TOP,fill=X)

        # create observer for upload
        upload_obs = UploadObserver(parent, controller)

        # state the template name
        tt1 = "Client Profile"
        # create a button observable
        obs1 = ButtonObservable()
        # create a button
        b1 = tk.Button(self, text=tt1,
                       command = lambda: obs1.raise_event(self))
        # set the button for the observable
        obs1.set_button(b1)
        # add the observer
        obs1.add_observer(upload_obs)
        b1.template = tt1
        # add the name
        b1.name = name
        b1.pack(side=TOP,fill=X)


        tt2 = "Needs Assessment & Referrals"
        obs2 = ButtonObservable()
        b2 = tk.Button(self, text=tt2,
                       command = lambda: obs2.raise_event(self))
        obs2.set_button(b2)
        obs2.add_observer(upload_obs)
        b2.template = tt2
        b2.name = name
        b2.pack(side=TOP, fill=X)


        tt3 = "Community Connections"
        obs3 = ButtonObservable()
        b3 = tk.Button(self, text=tt3,
                       command = lambda: obs3.raise_event(self))
        obs3.set_button(b3)
        obs3.add_observer(upload_obs)
        b3.template = tt3
        b3.name = name
        b3.pack(side=TOP, fill=X)


        tt4 = "Information and Orientation"
        obs4 = ButtonObservable()
        b4 = tk.Button(self, text=tt4,
                       command = lambda: obs4.raise_event(self))
        obs4.set_button(b4)
        obs4.add_observer(upload_obs)
        b4.template = tt4
        b4.name = name
        b4.pack(side=TOP, fill=X)

        tt5 = "Employment Related Services"
        obs5 = ButtonObservable()
        b5 = tk.Button(self, text=tt5,
                       command = lambda: obs5.raise_event(self))
        obs5.set_button(b5)
        obs5.add_observer(upload_obs)
        b5.template = tt5
        b5.name = name
        b5.pack(side=TOP, fill=X)

        tt6 = "Language Training - Client Enrol"
        obs6 = ButtonObservable()
        b6 = tk.Button(self, text=tt6,
                       command = lambda: obs6.raise_event(self))
        obs6.set_button(b6)
        obs6.add_observer(upload_obs)
        b6.template = tt6
        b6.name = name
        b6.pack(side=TOP, fill=X)

        tt7 = "Language Training - Course Setup"
        obs7 = ButtonObservable()
        b7 = tk.Button(self, text=tt7,
                       command = lambda: obs7.raise_event(self))
        obs7.set_button(b7)
        obs7.add_observer(upload_obs)
        b7.template = tt7
        b7.name = name
        b7.pack(side=TOP, fill=X)

        tt8 = "Language Training - Client Exit"
        obs8 = ButtonObservable()
        b8 = tk.Button(self, text=tt8,
                       command = lambda: obs8.raise_event(self))
        obs8.set_button(b8)
        obs8.add_observer(upload_obs)
        b8.template = tt8
        b8.name = name
        b8.pack(side=TOP, fill=X)


        back = Button(self, text="Back",
                            command=self.back)
        back.pack(side=TOP,fill=X)

    def back(self):
        self.cont.set_page(ap.AgencyPage, self.name)
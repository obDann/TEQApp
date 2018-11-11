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
        upload_obs = UploadObserver()

        template_1 = "Client Profile"
        obs_button1 = ButtonObservable()
        obs_button1.set_button(tk.Button(self, text=template_1,
                                         command = lambda: obs_button1.raise_event(self)))
        obs_button1.add_observer(upload_obs)
        b1 = obs_button1.button
        b1.template = template_1
        b1.pack(side=TOP,fill=X)

        template_2 = "Needs Assessment & Referrals"
        obs_button2 = ButtonObservable()
        obs_button2.set_button(tk.Button(self, text=template_2,
                                         command = lambda: obs_button2.raise_event(self)))
        obs_button2.add_observer(upload_obs)
        b2 = obs_button2.button
        b2.template = template_2
        b2.pack(side=TOP,fill=X)

        template_3 = "Community Connections"
        obs_button3 = ButtonObservable()
        obs_button3.set_button(tk.Button(self, text=template_3,
                                         command = lambda: obs_button3.raise_event(self)))
        obs_button3.add_observer(upload_obs)
        b3 = obs_button3.button
        b3.template = template_3
        b3.pack(side=TOP,fill=X)

        template_4 = "Information and Orientation"
        obs_button4 = ButtonObservable()
        obs_button4.set_button(tk.Button(self, text=template_4,
                                         command = lambda: obs_button4.raise_event(self)))
        obs_button4.add_observer(upload_obs)
        b4 = obs_button4.button
        b4.template = template_4
        b4.pack(side=TOP,fill=X)

        template_5 = "Employment Related Services"
        obs_button5 = ButtonObservable()
        obs_button5.set_button(tk.Button(self, text=template_5,
                                         command = lambda: obs_button5.raise_event(self)))
        obs_button5.add_observer(upload_obs)
        b5 = obs_button5.button
        b5.template = template_5
        b5.pack(side=TOP,fill=X)

        template_6 = "Language Training - Client Enrol"
        obs_button6 = ButtonObservable()
        obs_button6.set_button(tk.Button(self, text=template_6,
                                         command = lambda: obs_button6.raise_event(self)))
        obs_button6.add_observer(upload_obs)
        b6 = obs_button6.button
        b6.template = template_6
        b6.pack(side=TOP,fill=X)

        template_7 = "Language Training - Course Setup"
        obs_button7 = ButtonObservable()
        obs_button7.set_button(tk.Button(self, text=template_7,
                                         command = lambda: obs_button7.raise_event(self)))
        obs_button7.add_observer(upload_obs)
        b7 = obs_button7.button
        b7.template = template_7
        b7.pack(side=TOP,fill=X)

        template_8 = "Language Training - Client Exit"
        obs_button8 = ButtonObservable()
        obs_button8.set_button(tk.Button(self, text=template_8,
                                         command = lambda: obs_button8.raise_event(self)))
        obs_button8.add_observer(upload_obs)
        b8 = obs_button8.button
        b8.template = template_8
        b8.pack(side=TOP,fill=X)

        back = Button(self, text="Back",
                            command=self.back)
        back.pack(side=TOP,fill=X)

    def back(self):
        self.cont.set_page(ap.AgencyPage, self.name)

    def upload(self, template_name):
        '''
        (FileUploadPage, str) -> None

        Uploads a file to the database according to a specified template name
        '''
        # make a template handler

        # make another root
        temp_root = Tk()
        # inject the root into the FileSystemFetcher
        my_fsf = FileSystemFetcher(temp_root)
        the_dataframe = my_fsf.execute()
        temp_root.mainloop()
        print(the_dataframe)

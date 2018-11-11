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

        template_1 = "Client Profile"
        b1 = tk.Button(self, text=template_1,
                       command = lambda: self.upload(template_1))
        b1.pack(side=TOP,fill=X)

        template_2 = "Needs Assessment & Referrals"
        b2 = tk.Button(self, text=template_2,
                       command = lambda: self.upload(template_2))
        b2.pack(side=TOP,fill=X)

        template_3 = "Community Connections"
        b3 = tk.Button(self, text=template_3,
                       command = lambda: self.upload(template_3))
        b3.pack(side=TOP,fill=X)

        template_4 = "Information and Orientation"
        b4 = tk.Button(self, text=template_4,
                       command = lambda: self.upload(template_4))
        b4.pack(side=TOP,fill=X)

        template_5 = "Employment Related Services"
        b5 = tk.Button(self, text=template_5,
                       command = lambda: self.upload(template_5))
        b5.pack(side=TOP,fill=X)

        template_6 = "Language Training - Client Enrol"
        b6 = tk.Button(self, text=template_6,
                       command = lambda: self.upload(template_6))
        b6.pack(side=TOP,fill=X)

        template_7 = "Language Training - Course Setup"
        b7 = tk.Button(self, text=template_7,
                       command = lambda: self.upload(template_7))
        b7.pack(side=TOP,fill=X)

        template_8 = "Language Training - Client Exit"
        b8 = tk.Button(self, text=template_8,
                       command = lambda: self.upload(template_8))
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

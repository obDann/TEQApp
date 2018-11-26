import tkinter as tk
from tkinter import *
import sys
import research_ques_page as rqp
import client_type_page as ct
sys.path.insert(0, "../graphs")
from client_summary import *

class ClientSummaryReports(tk.Frame):
    def __init__(self, parent, controller, name):
        self.name = name
        self.cont = controller
        self.year = 0 # To restrict options down below
        tk.Frame.__init__(self,parent)
        Label(self, text="Choose Report").grid(row=1)
        
        # options menu to select type of report
        report_choice = {"Client Types","Language Perference", 
                         "Methods of Communication"}
        self.report = StringVar(self)
        self.report.set("Options")
        menu = OptionMenu(self, self.report, *report_choice)
        menu.grid(row=1, column=1)
        
        b1 = Button(self, text="Confirm", command=lambda: 
                    self.check(self.report.get()))
        b1.grid(row=2, column=1, sticky=W, pady=6)      
        
        back = Button(self, text="Back",command=lambda: 
                      controller.set_page(rqp.ResearchQuesPage, self.name))
        back.grid(row=5, column=1, sticky=W, pady=6)
    
    def check(self, report):
        if (report == "Language Perference"):  
            client_language_pref()
        elif (report == "Methods of Communication"):
            phone_vs_email_usage()
        elif (report == "Client Types"):
            self.cont.set_page(ct.ClientTypePage,self.name)

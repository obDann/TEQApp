import tkinter as tk
from tkinter import *
import sys
import research_ques_page as rqp
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
        report_choice = {"Client Agencies","Language Perference", 
                         "Ways of Communication"}
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
        if (report == "Client Agencies"):
            self.year = 1
        self.show_options()    

    def show_options(self):
        if (self.year == 1):
            Label(self, text="Year: ").grid(row=3)
            month = {"01","02","03","04","05","06","07","08","09","10","11","12"}
            self.month_c =StringVar(self)
            self.month_c.set("Month")
            menu = OptionMenu(self, self.month_c, *month)
            menu.grid(row=3, column=3)
        
            e1 = Entry(self)
            e1.grid(row=3,column=1)
            # Get the text input
            self.year_c = e1.get()
            
            b2 = Button(self, text="Generate Report", 
                    command=lambda: self.display())
            b2.grid(row=5, column=2, sticky=W, pady=6)
            
    def display(self):
        report = self.report.get()
        if (report == "Language Perference"):
            client_language_pref()
        elif (report == "Client Agencies"):
            client_agency(str(self.year_c), str(self.month_c))
        elif (report == "Ways of Communication"):
            phone_vs_email_usage()

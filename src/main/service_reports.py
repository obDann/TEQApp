import tkinter as tk
from tkinter import *
import sys
import research_ques_page as rqp
import find_years
sys.path.insert(0, "../graphs")
from display_graphs import *

default = '-----'

class ServiceReports(tk.Frame):
    def __init__(self, parent, controller, name):
        self.name = name
        self.cont = controller
        self.year = 0 # if user selects graph that uses years menu
        tk.Frame.__init__(self,parent)
        
        Label(self, text="Choose Report").grid(row=1)
        
        # options menu to select type of report
        self.report = StringVar(self)
        report_choice = {"Age of Clients", "Number of Clients in Each Month"}
        self.report.set("Age of Clients")
        menu = OptionMenu(self, self.report, *report_choice)
        menu.grid(row=1, column=1)
        
        # options menu to select what service
        self.service = StringVar(self)
        service_choice = {"Community Connections", "Information & Orientation", 
                  "Employment Related Service"}
        self.service.set("Community Connections")
        self.ser_menu = OptionMenu(self, self.service, *service_choice)        
        
        b1 = Button(self, text="Confirm", command=lambda: 
                    self.check_report(self.report.get()))
        b1.grid(row=2, column=1, sticky=W, pady=6)      
        
        back = Button(self, text="Back",command=lambda: 
                      controller.set_page(rqp.ResearchQuesPage, self.name))
        back.grid(row=5, column=1, sticky=W, pady=6)
    
    def check_report(self,report):
        Label(self, text="Service").grid(row=3)
        
        # options menu to select service
        self.ser_menu.grid(row=3, column=1)
        
        if (report == "Number of Clients in Each Month"):
            self.year = 1
        else:
            self.year = 0
        self.show_options()
        self.check_year()
    
    def show_options(self):
        '''
        Show Year Menu bar and Generate Report button.
        '''
        Label(self, text="Year").grid(row=4)
        # options menu to select year
        self.year_c = StringVar(self)          
        # finds the years that are available for reports
        years = find_years.find_years()
        self.year_choice = set()
        self.year_c.set(default)
        if (len(years) > 0):
            for year in years:
                self.year_choice.add(year)
        # if no data is in the database, no options are given
        if (len(self.year_choice) == 0):
            self.year_choice = {default}
        self.menu = OptionMenu(self, self.year_c, *self.year_choice)
        self.menu.grid(row=4, column=1)
        
        b2 = Button(self, text="Generate Report", 
                    command=lambda: self.display_graph())
        b2.grid(row=5, column=2, sticky=W, pady=6)        
    
    def check_year(self):
        '''
        Disables the Year option if user selected a different report.
        '''
        if (self.year == 0):
            self.year_c.set(default)
            self.menu.configure(state="disabled")
    
    def display_graph(self):
        # convert choices for table name in the database
        service = self.service.get()
        if (service == "Community Connections"):
            val = "Community_Connections"
        elif (service == "Information & Orientation"):
            val = "Info_and_Orientation"
        elif (service == "Employment Related Service"):
            val = "Employment_Service"

        if (self.year == 1 and self.year_c.get() != default):
            num_clients(self.year_c.get(), val, service)
        elif (self.year == 0):
            age_histogram(val, service)
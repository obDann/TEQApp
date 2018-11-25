import tkinter as tk
from tkinter import *
import reports_page as rp
import service_reports as sr
import client_summary_reports as cs
import sys
sys.path.insert(0, "../graphs")
from display_graphs import *

class ResearchQuesPage(tk.Frame):
    def __init__(self, parent, controller, name):
        self.name = name
        self.cont = controller
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Please select one of the " + 
                         "following reports")
        label.pack(side=TOP,fill=X)
        
        b1 = Button(self, text="Service Reports", 
                    command=lambda: controller.set_page(sr.ServiceReports, 
                                                     self.name))
        b1.pack(side=TOP,fill=X)
        
        b2 = Button(self, 
                    text="Clients with Children in Language Training Course",
                    command=lambda: self.child_report())
        b2.pack(side=TOP,fill=X)
        
        b3 = Button(self, text="Transportation", 
                    command=lambda: self.transport_report())
        b3.pack(side=TOP,fill=X)
        
        b4 = Button(self, text="Referral Age Groups",
                    command=lambda: self.referral_age())
        b4.pack(side=TOP,fill=X)
        
        b5 = Button(self, text="Referral", command=lambda: self.referral_cs())
        b5.pack(side=TOP,fill=X)
        
        b6 = Button(self, text="Client Reports", command=lambda:
                    controller.set_page(cs.ClientSummaryReports, self.name))
        b6.pack(side=TOP,fill=X)
        
        back = Button(self, text="Back",
                            command=lambda: controller.set_page(rp.ReportsPage, 
                                                             self.name))
        back.pack(side=TOP,fill=X)
    
    def child_report(self):
        child_pie()
    
    def transport_report(self):
        tran_pie()
    
    def referral_age(self):
        referral_age()
    
    def referral_cs(self):
        referral_citizenship()

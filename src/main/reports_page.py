import tkinter as tk
from tkinter import *
import teq_page as tp
import research_ques_page as rqp
import custom_query_page as cq

class ReportsPage(tk.Frame):
    def __init__(self, parent, controller, name):
        self.name = name
        self.cont = controller
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Please select one of the following")
        label.pack(side=TOP,fill=X)
        
        b1 = Button(self, text="Answer Research Questions",
                    command=lambda: controller.set_page(rqp.ResearchQuesPage, 
                                                     self.name))
        b1.pack(side=TOP,fill=X)
        
        b2 = Button(self, text="Generate Custom Queries", 
                    command=lambda: self.cont.set_page(cq.CustomQueryPage, 
                                                       self.name))
        b2.pack(side=TOP,fill=X)
        
        b3 = Button(self, text="Predictive Analysis")
        b3.pack(side=TOP,fill=X)      
        
        back = Button(self, text="Back",
                            command=lambda: controller.set_page(tp.TEQPage, 
                                                             self.name))
        back.pack(side=TOP,fill=X)        
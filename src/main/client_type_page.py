import tkinter as tk
from tkinter import *
import sys
import research_ques_page as rqp
sys.path.insert(0, "../graphs")
from client_summary import *

class ClientTypePage(tk.Frame):
    def __init__(self, parent, controller, name):
        self.name = name
        self.cont = controller
        self.year = 0 # To restrict options down below
        tk.Frame.__init__(self,parent)
        
        Label(self, text="Year: ").grid(row=1)
        month = {"01","02","03","04","05","06","07","08","09","10","11","12"}
        self.month_c =StringVar(self)
        self.month_c.set("Month")
        menu = OptionMenu(self, self.month_c, *month)
        menu.grid(row=1, column=2)
    
        self.text = Text(self,width=5, height=1)
        self.text.grid(row=1,column=1)
        
        b2 = Button(self, text="Generate Report", 
                command=lambda: self.display())
        b2.grid(row=3, column=2, sticky=W, pady=6)        
        
        back = Button(self, text="Back",command=lambda: 
                      controller.set_page(rqp.ResearchQuesPage, self.name))
        back.grid(row=3, column=1, sticky=W, pady=6)        
            
    def display(self):
        client_types(self.retrieve_input(), self.month_c.get())
        
    def retrieve_input(self):
        '''
        Gets the year in text.
        '''
        input_value = self.text.get("1.0","end-1c")
        return input_value        
        
import tkinter as tk
from tkinter import ttk
import pandas as pd
import agency_page as ap
from table_viewer_page import *

'''
class My_GUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        self.cont = tk.Frame(self)
        self.cont.pack(side="top", fill="both", expand = True)
        self.cont.grid_rowconfigure(0, weight=1)
        self.cont.grid_columnconfigure(0, weight=1)
        self.set_page(DataViewerPage, "Name")
    
    def display(self, page):
        frame = page(self.cont, self)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()
            
    def set_page(self, f, name):
        frame = f(self.cont, self, name)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()
'''

class DataViewerPage(tk.Frame):
    
    # from https://stackoverflow.com/questions/44798950/how-to-display-a-dataframe-in-tkinter
    def __init__(self, parent, controller, data_frame, temp_name, month, year):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.data_f = data_frame
        self.temp_n = temp_name
        self.m = month
        self.y = year
        label1 = tk.Label(self, text="Data Viewer")
        label1.pack(side="top", fill="x", pady=10)        
        
        b1 = tk.Button(self, text="Generate Table", command=lambda: 
                       self.controller.set_page(TableViewer(self.data_f, 
                                                self.temp_n, self.m, self.y)))
        b1.pack()
        
        back = tk.Button(self, text="Back",command=lambda: 
                         self.controller.set_page(ap.AgencyPage))
        back.pack()

'''
if __name__ == "__main__":
    app = My_GUI()
    app.mainloop()
'''
import tkinter as tk
from tkinter import ttk
import pandas as pd
import agency_page as ap
from table_viewer_page import *

class DataViewerPage(tk.Frame):
    
    # from https://stackoverflow.com/questions/44798950/how-to-display-a-dataframe-in-tkinter
    def __init__(self, parent, controller, data_frame, temp_name, month, year, name):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.data_f = data_frame
        self.temp_n = temp_name
        self.m = month
        self.y = year
        self.name = name
        label1 = tk.Label(self, text="Data Viewer")
        label1.pack(side="top", fill="x", pady=10)        
        
        b1 = tk.Button(self, text="Generate Table", command=lambda: 
                       self.controller.insert_page_details(TableViewer, 
                                                self.data_f, 
                                                self.temp_n, self.m,
                                                self.y, self.name))
        b1.pack()
        
        back = tk.Button(self, text="Back",command=lambda: 
                         self.controller.set_page(ap.AgencyPage, self.name))
        back.pack()

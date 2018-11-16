import tkinter as tk
from tkinter import ttk
import pandas as pd
from agency_page import * 
from table_viewer_page import *

class DataViewerPage(tk.Frame):
    
    # from https://stackoverflow.com/questions/44798950/how-to-display-a-dataframe-in-tkinter
    def __init__(self, parent, controller, data_frame, temp_name):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.df = data_frame
        self.template_name = temp_name
        label1 = tk.Label(self, text="Data Viewer")
        label1.pack(side="top", fill="x", pady=10)        
           
        b1 = tk.Button(self, text="Generate Table",
                            command=lambda: controller.display(TableViewer))
        b1.pack()
        
        back = tk.Button(self, text="Back",
                         command=lambda: controller.display(AgencyPage))
        back.pack()

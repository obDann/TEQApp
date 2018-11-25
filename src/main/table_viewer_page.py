import tkinter as tk
from tkinter import ttk
import pandas as pd
import agency_page as ap 
from data_viewer_page import *
import sys
sys.path.append("../commands")
import missing_val_checker as mv
import data_aggregator as da
sys.path.append("../database")
import beautiful_uploader as bu
sys.path.append("../temhelp")
from true_tem_handler import TrueTemplateHandler as tth

class TableViewer(tk.Frame): 
    
    def __init__(self, parent, controller, data_frame, temp_name, month, year):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.df = data_frame
        self.temp_name = temp_name
        # month and year for some templates
        self.m = month
        self.y = year
        
        # Run the checkers
        self._execute_checkers()
        
        # The title
        label1 = tk.Label(self, text=self.temp_name)
        label1.pack(side="top", fill="x", pady=10)
        
        # The column selection drop down box
        tk.Label(self, text='Select Column:').pack()
        self.options = ttk.Combobox(self, values=list(self.df.columns))
        self.options.pack(pady=10)
        
        b1 = tk.Button(self, text='Show Data', command=self.show_option)
        b1.pack()
        
        label2 = tk.Label(self, text = "The Data Will be Shown below:")
        label2.pack(pady=5)
        
        # The text box at the bottom
        self.text = tk.Text(self)
        self.text.pack()
        
        b2 = tk.Button(self, text='Save', command=lambda: self.save_data())
        b2.pack()
        
        # Uploads the data to db and 
        back = tk.Button(self, text="Back",
                         command=lambda: [self.upload_data(),
                                      self.controller.set_page(ap.AgencyPage)])
        back.pack()        
   
    def show_option(self):
        '''
        Shows the list of options for this table
        '''
        identifier = self.options.get() # get option
        self.text.delete(1.0, tk.END)   # empty widget to print new text
        self.text.insert(tk.END, str(self.df[identifier])) 
    
    def _execute_checkers(self):
        '''
        Executes the checkers for mis matched data.
        '''
        template_handler = tth.TrueTemplateHandler(self.template_name)
        
        temp_mv = mv.MissingValChecker(self.template_name)
        temp_da = da.DataAggregator(self.template_name)
        self.df = mv.execute(self.df, template_handler)
        self.df = da.execute(self.df, template_handler) 
        
    def save_data(self):
        '''
        Saves the display column values as a DataFrame and return the whole
        DataFrame.
        '''
        new_col = list()
        # Get the column name
        ind = self.options.get()
        
        # For formatting where index 0 is empty and index 1 is column name
        new_col.append("")
        new_col.append(ind)
        
        # Get the text input
        inputValue = self.text.get("1.0","end-1c")
        # Split them into a list
        temp_text = inputValue.split('\n')
        
        # Edit the split list to only contain the values
        for element in temp_text:
            element = element.strip()
            element = element.split(' ')
            new_col.append(element[len(element)-1])
            
        # Remove the last element since that is the dtype
        new_col = pd.DataFrame(new_col[:len(new_col)-1], columns=[ind])
        # Add it back to the original dataFrame
        self.df = self.df.update(new_col)
    
    def upload_data(self):
        '''
        Uploads the saved data onto our database.
        '''
        
        beaut_up = bu.BeautifulUploader()
        if (self.temp_name == "Client Profile"):
            beaut_up.upload_client_profile(self.df)
        elif (self.temp_name == "Needs Assessment & Referrals"):
            beaut_up.upload_needs_referrals(self.df)
        elif (self.temp_name == "Community Connections"):
            beaut_up.upload_community_connections(self.df, self.m , self.y)
        elif (self.temp_name == "Employment Related Services"):
            bu.upload_info_ori(self.df, self.m , self.y)
        elif (self.temp_name == "Language Training - Client Enrol"):
            beaut_up.upload_employment_service(self.df, self.m , self.y)
        elif (self.temp_name == "Language Training - Course Setup"):
            beaut_up.upload_LT_client_enrol(self.df)
        elif (self.temp_name == "Language Training - Client Exit"):
            beaut_up.upload_LT_course_setup(self.df)
import tkinter as tk
from tkinter import ttk
import pandas as pd
from agency_page import * 
from data_viewer_page import *
from table_observer import *
from button_observable import *
import sys
sys.path.append("../commands")
import missing_val_checker as mv
import data_aggregator as da


class TableViewer(tk.Frame): 
    
    def __init__(self, parent, controller, data_frame, temp_name):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.df = data_frame
        self.template_name = temp_name        
        
        # Run the checkers
        self._execute_checkers()
        
        # The title
        label1 = tk.Label(self, text=temp_name)
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

        back = tk.Button(self, text="Back",
                         command=lambda: controller.display(AgencyPage))
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
        temp_mv = mv.MissingValChecker(self.template_name)
        temp_da = da.DataAggregator(self.template_name)
        self.df = mv.execute(self.df, self.template_name)
        self.df = da.execute(self.df,self.template_name) 
        
    def save_data(self):
        '''
        Saves the display column values as a DataFrame and return the whole
        DataFrame.
        '''
        new_col = list()
                    
        # Get the column name
        ind = self.options.get()
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
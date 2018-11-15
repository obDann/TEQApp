import tkinter as tk
from tkinter import ttk
import pandas as pd

class DataViewerPage(tk.Frame):
    
    # from https://stackoverflow.com/questions/44798950/how-to-display-a-dataframe-in-tkinter
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label1 = tk.Label(self, text="Data Viewer")
        label1.pack(side="top", fill="x", pady=10)        
           
        b1 = tk.Button(self, text="Generate Table",
                            command=lambda: controller.display(TableViewer))
        b1.pack()
        
class TableViewer(tk.Frame): 

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        # The title
        label1 = tk.Label(self, text="Excel Data Displayer")
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

        # Back Button
        b2 = tk.Button(self, text="Back",
                  command=lambda: controller.display(DataViewerPage))
        b2.pack()
        
        b3 = tk.Button(self, text='Save', command=lambda: self.save_data())
        b3.pack()

   
    def show_option(self):
        identifier = self.options.get() # get option
        self.text.delete(1.0, tk.END)   # empty widget to print new text
        self.text.insert(tk.END, str(self.df[identifier]))    

    def save_data(self):
        '''
        () -> DataFrame
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
        new_df = df.update(new_col)
        return new_df
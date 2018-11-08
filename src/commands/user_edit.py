import tkinter as tk
from tkinter import *
import pandas as pd

def popup_user_edit():
    '''
    This function is for the user input
    '''
    
def popup_data_column():
    '''
    This function is for the data row
    '''

class Application(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.pack()      
        
        text = tk.Text(self)
        text.insert(tk.END, str(df))
        text.pack()
        


root = tk.Tk()
app = Application(root)
root.mainloop()
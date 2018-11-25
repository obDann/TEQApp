import tkinter as tk
from tkinter import *
from tkinter import ttk
import random
import csv
import sqlite3
import reports_page as rp

class CustomQueryPage(tk.Frame):
    def __init__(self, parent, controller, name):
        self.name = name
        self.cont = controller
        tk.Frame.__init__(self,parent)
        label1 = tk.Label(self, text="Enter Your Command Here:")
        label1.pack(side=TOP,anchor=NW, padx=10)
        
        # The text box at the bottom
        self.text1 = tk.Text(self,width=80, height=1)
        self.text1.pack(side=TOP,fill=X, padx=10)
        label2 =  tk.Label(self, text = "Name of the file: ")
        label2.pack(side=TOP,anchor=NW, padx=10)
        self.text2 = tk.Text(self,width=10, height=1)
        self.text2.pack(side=TOP,fill=X, padx=10)        
        
        b1 = tk.Button(self, text="Save",
                       command=lambda: self.export_to_csv())
                                
        b1.pack(side=TOP,fill=X, padx= 5, pady= 5)
    
        back = tk.Button(self, text="Back",command=lambda: 
                         controller.set_page(rp.ReportsPage, self.name))
        back.pack(side=TOP,fill=X, padx = 5, pady=5) 
    
    def export_to_csv(self):
        '''
        Export the selected query into a csv file.
        '''
        temp_num = str(randint(1, 9999))
        # Establish a sqlite connection
        conn = sqlite3.connect('client_data.db')
        cur = conn.cursor()
        file_name = self.retrieve_fn_input().strip()
        if (file_name == "" or file_name == None):
            file_name = "CSV"+str(temp_num)
        try:
            # Get the user query
            query = self.retrieve_SQL_input()
            cur.execute(query)
            result = cur.fetchall()
            # Write the result into a csv file
            with open(file_name +'.csv', "w", newline='') as csv_file: 
                writer = csv.writer(csv_file, delimiter=',')
                for line in result:
                    writer.writerow(line)                
        except sqlite3.Error as e:
            print("Invalid SQL input, with the message: " + e)
        # Finish message
        print("Finished executing query.")
        
        
    def retrieve_SQL_input(self):
        '''
        Gets the SQL Command in text.
        '''
        input_value = self.text1.get("1.0","end-1c")
        return input_value
    
    def retrieve_fn_input(self):
        '''
        Gets the File name in text.
        '''
        input_value = self.text2.get("1.0","end-1c")
        return input_value    

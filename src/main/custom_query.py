import tkinter as tk
from tkinter import *
from tkinter import ttk
import random
#import teq_page as tp
from custom_query_observer import *
from button_observable import *


class My_GUI(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        self.cont = tk.Frame(self)

        self.cont.pack(side="top", fill="both", expand = True)

        self.cont.grid_rowconfigure(0, weight=1)
        self.cont.grid_columnconfigure(0, weight=1)

        self.display(CustomQueryPage)
    
    def display(self, page):
        frame = page(self.cont, self)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()
            
    def set_page(self, f, name):
        frame = f(self.cont, self, name)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()


class CustomQueryPage(tk.Frame):
    def __init__(self, parent, controller):
        self.cont = controller
        tk.Frame.__init__(self,parent)
        label1 = tk.Label(self, text="Enter Your Command Here:")
        label1.pack(side=TOP,anchor=NW, padx=10)
        
        cq_obs = CustomQueryObserver()
        
        # The text box at the bottom
        self.text1 = tk.Text(self,width=80, height=1)
        self.text1.pack(side=TOP,fill=X, padx=10)
        label2 =  tk.Label(self, text = "Name of the file: ")
        label2.pack(side=TOP,anchor=NW, padx=10)
        self.text2 = tk.Text(self,width=10, height=1)
        self.text2.pack(side=TOP,fill=X, padx=10)        
        
        obs_button1 = ButtonObservable()
        obs_button1.set_button(tk.Button(self, text="Save",
                            #command=lambda: obs_button1.raise_event(self)))
                            command=lambda: self.export_to_csv()))
                            
        obs_button1.add_observer(cq_obs)
        save = obs_button1.button        
        save.pack(side=TOP,fill=X, padx= 5, pady= 5)
    
        back = tk.Button(self, text="Back")
                         #command=lambda: controller.display(tp.TEQPage))
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
        except TypeError as e:
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
        
        
if __name__ == "__main__":
    app = My_GUI()
    app.mainloop()
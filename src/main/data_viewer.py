import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont 
import pandas as pd

class My_GUI(tk.Tk):

    # from https://stackoverflow.com/questions/44798950/how-to-display-a-dataframe-in-tkinter
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (DataViewerPage, TableViewer):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame


            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("DataViewerPage")

    def show_frame(self, page_name):
        '''
        Show a Tk frame based on the given page name
        '''
        frame = self.frames[page_name]
        frame.tkraise()

class DataViewerPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label1 = tk.Label(self, text="Data Viewer", font=controller.title_font)
        label1.pack(side="top", fill="x", pady=10)

        b1 = tk.Button(self, text="Generate Table",
                            command=lambda: controller.show_frame("TableViewer"))
        b1.pack()


class TableViewer(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # The title
        label1 = tk.Label(self, text="Template Name", font=controller.title_font)
        label1.pack(side="top", fill="x", pady=10)
        
        # The column selection drop down box
        tk.Label(self, text='Select Column:').pack()
        self.options = ttk.Combobox(self, values=list(df.columns))
        self.options.pack(pady=10)
        b1 = tk.Button(self, text='Show Data', command=self.show_option)
        b1.pack()
        
        label2 = tk.Label(self, text = "The Data Will be Shown below:")
        label2.pack(pady=5)
        
        # The text box at the bottom
        self.text = tk.Text(self)
        
        # Back Button
        self.text.pack()
        b2 = tk.Button(self, text="Back",
                  command=lambda: controller.show_frame("DataViewerPage"))
        b2.pack()
   
    def show_option(self):
        identifier = self.options.get() # get option
        self.text.delete(1.0, tk.END)   # empty widget to print new text
        self.text.insert(tk.END, str(df[identifier]))    

a = {'ISBN':[150,82.50,150,157.50,78.75],
     'Year':[245,134.75,245,257.25,128.63]}
df = pd.DataFrame(a,index=['a','b', 'c', 'd','e']) 

#print(df.iloc[:6,1:2])

if __name__ == "__main__":
    app = My_GUI()
    app.mainloop()
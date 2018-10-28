import tkinter as tk
from tkinter import *
import client_db_functions

#from https://pythonprogramming.net/change-show-new-frame-tkinter/
#for class structure and init arguments
class TeqApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        self.cont = tk.Frame(self)

        self.cont.pack(side="top", fill="both", expand = True)

        self.cont.grid_rowconfigure(0, weight=1)
        self.cont.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (MainPage, LoginPage, CreateAcc):

            frame = F(self.cont, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.display(MainPage)

    def display(self, cont):

        frame = self.frames[cont]
        frame.tkraise()
        
    def set_page(self, f, name):
        frame = f(self.cont, self, name)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()
        

class MainPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Please choose one of the following:")
        label.pack(side=TOP,fill=X)

        b1 = tk.Button(self, text="Login",
                            command=lambda: controller.display(LoginPage))
        b1.pack(side=TOP,fill=X)

        b2 = tk.Button(self, text="Create a New Account",
                            command=lambda: controller.display(CreateAcc))
        b2.pack(side=TOP,fill=X)

class LoginPage(tk.Frame):

    def __init__(self, parent, controller):
        self.cont = controller
        tk.Frame.__init__(self, parent)
        
        Label(self, text="Username").grid(row=1)
        Label(self, text="Password").grid(row=2)
        
        self.e1 = Entry(self)
        self.e1.grid(row=1, column=1)
        self.e2 = Entry(self, show="*")
        self.e2.grid(row=2, column=1)
        
        b1 = Button(self, text="Back",
                            command=lambda: self.cont.display(MainPage))
        b1.grid(row=5, column=1, sticky=W, pady=6)
        
        b2 = Button(self, text="Login", command=self.log_user)
        b2.grid(row=5, column=2, sticky=W, pady=6)
    
    def log_user(self):
        username = self.e1.get()
        pw = self.e2.get()
        
        if (username != "" and pw != ""):
            # grab name and type of acc if login as successful
            (name, acc) = client_db_functions.login(username, pw)
            if (name != None and acc != None):
                self.check_type(name, acc)
    
    def check_type(self, name, acc):
        if (acc == "Agency"):
            self.cont.set_page(AgencyPage, name)
        elif (acc == "TEQ"):
            self.cont.set_page(TEQPage, name)
        else:
            self.cont.set_page(AdminPage, name)

class CreateAcc(tk.Frame):

    def __init__(self, parent, controller):
        self.cont = controller
        tk.Frame.__init__(self, parent)
        
        Label(self, text="Username").grid(row=1)
        Label(self, text="First Name").grid(row=2)
        Label(self, text="Password").grid(row=3)
        Label(self, text="Choose an Account").grid(row=4)
        
        self.e1 = Entry(self)
        self.e1.grid(row=1, column=1)
        self.e2 = Entry(self)
        self.e2.grid(row=2, column=1)
        self.e3 = Entry(self, show="*")
        self.e3.grid(row=3, column=1)
        
        # Options menu for selecting which account
        self.acc = StringVar(self)
        choice = {"Agency", "TEQ", "Admin"}
        self.acc.set("Agency")
        menu = OptionMenu(self, self.acc, *choice)
        menu.grid(row=4, column=1)
        
        b1 = Button(self, text="Back",
                            command=lambda: self.cont.display(MainPage))
        b1.grid(row=5, column=1, sticky=W, pady=6)
        
        b2 = Button(self, text="Submit", command=self.create_user)
        b2.grid(row=5, column=2, sticky=W, pady=6)
        
    def create_user(self):
        username = self.e1.get()
        name = self.e2.get()
        pw = self.e3.get()
        acc = self.acc.get()
        
        if (username != "" and name != "" and pw != ""):
            client_db_functions.insert_user(username, name, pw, acc)
            self.cont.display(MainPage)
        
class AgencyPage(tk.Frame):
    def __init__(self, parent, controller, name):
        self.cont = controller
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Hello " + name + 
                         ". What would you like to do?")
        label.pack(side=TOP,fill=X)
        
        b1 = tk.Button(self, text="Submit iCare File",
                            command=lambda: self.cont.set_page(FileUpload, name))
        b1.pack(side=TOP,fill=X)
        
        back = Button(self, text="Back",
                            command=lambda: self.cont.display(MainPage))
        back.pack(side=TOP,fill=X)        

class TEQPage(tk.Frame):
    def __init__(self, parent, controller, name):
        self.cont = controller
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Hello " + name + 
                         ". What would you like to do?")
        label.pack(side=TOP,fill=X)
        
        back = Button(self, text="Back",
                            command=lambda: self.cont.display(MainPage))
        back.pack(side=TOP,fill=X)         

class AdminPage(tk.Frame):
    def __init__(self, parent, controller, name):
        self.cont = controller
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Hello " + name + 
                         ". What would you like to do?")
        label.pack(side=TOP,fill=X)
        
        back = Button(self, text="Back",
                            command=lambda: self.cont.display(MainPage))
        back.pack(side=TOP,fill=X)         

class FileUpload(tk.Frame):

    def __init__(self, parent, controller, name):
        self.cont = controller
        self.name = name
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Choose a type to upload:")
        label.pack(side=TOP,fill=X)
        
        #Buttons dont work
        b1 = tk.Button(self, text="Client Profile")
        b1.pack(side=TOP,fill=X)

        b2 = tk.Button(self, text="Needs Assessment & Referrals")
        b2.pack(side=TOP,fill=X)
        
        b3 = tk.Button(self, text="Community Connections")
        b3.pack(side=TOP,fill=X)
        
        b4 = tk.Button(self, text="Information and Orientation")
        b4.pack(side=TOP,fill=X)
        
        b5 = tk.Button(self, text="Employment Related Services")
        b5.pack(side=TOP,fill=X) 
        
        b6 = tk.Button(self, text="Language Training - Client Enrol")
        b6.pack(side=TOP,fill=X)   
        
        b7 = tk.Button(self, text="Language Training - Course Setup")
        b7.pack(side=TOP,fill=X) 
        
        b8 = tk.Button(self, text="Language Training - Client Exit")
        b8.pack(side=TOP,fill=X) 
        
        back = Button(self, text="Back",
                            command=self.back)
        back.pack(side=TOP,fill=X)
    
    def back(self):
        self.cont.set_page(AgencyPage, self.name)

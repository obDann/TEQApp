from Observer import Observer
from tkinter import *
import tkinter.messagebox
import client_db_functions
import main_page as mp
import re
import sys
sys.path.insert(0, "../emailer")
from account_creation_emailer import *


class CreateUserObserver(Observer):
    '''
    Observer object for button that creates a new user
    '''
    
    def __init__(self):
        ''' (CreateUserObserver) -> None

        Initializes a CreateUserObserver object
        '''

    def notify(self, obs):
        ''' (CreateUserObserver, Observable) -> None

        If all values are filled, adds a new user record to the db
        and displays the main page
        '''
        username = obs.button.e1.get().lower()
        email = obs.button.e2.get().lower()
        name = obs.button.e3.get()
        pw = obs.button.e4.get()
        acc = obs.button.acc.get()

        if (username != "" and re.match(r"[^@]+@[^@]+\.[^@]+", email) and
                name != "" and pw != ""):
            error = False
            # check duplicate and return boolean for success and duplicates
            success = client_db_functions.check_duplicate(username, email)
            if (success[0]):
                client_db_functions.insert_user(username, email, name, pw, acc)
                emailer = AccountCreationEmailer()
                emailer.send(email)
                obs.page.cont.display(mp.MainPage)
            self.message(error, success[0], username = success[1],
                         email = success[2])
        else:
            error, success = True, False
            self.message(error, success, username, email, name, pw)

    def message(self, error, success, username="", email="", name="", pw=""):
        ''' (CreateUserObserver, bool, bool, str, str, str, str) -> None
        username, email, name and pw are optional parameters

        Creates a message box telling the user if the account was successfully
        created or not and additional error messages. error = False means it
        was successful
        '''
        if (error):
            title = "Error"
            msg = "Make sure the following fields are filled in properly: \n"
            entered_fields = [username, email, name, pw]
            fields = ["Username", "Email", "First Name", "Password"]
            for i in range(len(fields)):
                if (i == 1 and not re.match(r"[^@]+@[^@]+\.[^@]+", email)):
                    # if i is checking email field
                    msg += fields[i] + " (follow example@domain.ca format)\n"
                elif entered_fields[i] == "":
                    msg += fields[i] + "\n"
        else:
            if (success):
                title = "Confirm"
                msg = "Your account has been successfully created!"
            else:
                title = "Error"
                msg = "The following fields are already in use:\n"
                if (username != ""):
                    msg += "Username\n"
                if (email != ""):
                    msg += "Email\n"

        tkinter.messagebox.showinfo(title, msg)


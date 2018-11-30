from Observer import Observer
from tkinter import *
import tkinter.messagebox
sys.path.insert(0, "../accounts_database")
import client_db_functions
import main_page as mp
import re


class DeleteAccountObserver(Observer):
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

        if (username != ""):
            result = client_db_functions.delete_user(username)
            self.message(result[0], result[1])
        else:
            # runs the empty entry message
            self.message(False, True)

    def message(self, exists, agency):
        ''' (CreateUserObserver, bool, bool) -> None
        Creates a message box telling the user if the account was deleted or
        not.
        '''
        if(exists):
            if(agency):
                title = "Success"
                msg = "The account has been successfully deleted."
            else:
                title = "Error"
                msg = "You can only delete Agency accounts."
        else:
            title = "Error"
            if(agency):
                msg = "Please fill in all the fields."
            else:
                msg = "This username does not exist."

        tkinter.messagebox.showinfo(title, msg)
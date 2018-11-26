from Observer import Observer
import client_db_functions
import main_page as mp
from change_password_page import *


class ChangePasswordObserver(Observer):
    '''
    Observer object for button that creates a new user
    '''

    def __init__(self):
        ''' (ChangePasswordObserver) -> None

        Initializes a CreateUserObserver object
        '''

    def notify(self, obs):
        ''' (ChangePasswordObserver, Observable) -> None

        If all values are filled, checks if the passwords are the same and then
        updates the database if they are identical.
        '''
        password = obs.button.e1.get()
        confirm = obs.button.e2.get()

        if (password != "" and password == confirm):
            client_db_functions.update_pass(obs.button.user, password)
            client_db_functions.remove_temp(obs.button.user)
            obs.page.cont.display(mp.MainPage)
            self.message(False)
        else:
            self.message(True)

    def message(self, error):
        ''' (CreateUserObserver, bool) -> None

        Creates a message box telling the user if the password was successfully
        changed. error = False means it was successful
        '''
        if (error):
            title = "Error"
            msg = "Your password must match the one in the confirmation field."
        else:
            title = "Confirm"
            msg = "Your password was successfully changed."

        tkinter.messagebox.showinfo(title, msg)

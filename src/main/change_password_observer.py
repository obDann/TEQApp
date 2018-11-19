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

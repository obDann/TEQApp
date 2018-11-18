from Observer import Observer
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
            client_db_functions.insert_user(username, email, name, pw, acc)
            emailer = AccountCreationEmailer()
            emailer.send(email)
            obs.page.cont.display(mp.MainPage)

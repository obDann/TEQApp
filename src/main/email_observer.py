from Observer import Observer
import client_db_functions
import main_page as mp
from login_page import *
import re
import sys
sys.path.insert(0, "../emailer")
from password_forgetting_emailer import *


class EmailObserver(Observer):
    '''
    Observer object for sending an email to the person who forgot their
    password
    '''

    def __init__(self):
        ''' (EmailObserver) -> None
        
        Initializes a EmailObserver object
        '''

    def notify(self, obs):
        ''' (EmailObserver, Observable) -> None
        
        If the email exists, then the email will be sent to the appropriate
        email address
        '''
        email = obs.button.e1.get().lower()

        if (email != ""):
            # checking if email exists first
            found = client_db_functions.check_email(email)
            if (found):
                emailer = PasswordForgettingEmailer()
                emailer.send(email)
                obs.page.cont.display(mp.LoginPage)

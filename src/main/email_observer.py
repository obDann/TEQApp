from Observer import Observer
import client_db_functions
import login_page
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
        
        If all values are filled and correct, logs in
        the appropriate user
        '''
        email = obs.button.e1.get().lower()

        if (email != ""):
            # grab name and type of acc if login was successful
            found = client_db_functions.check_email(email)
            if (found):
                emailer = PasswordForgettingEmailer()
                # emailer.send(emailer)
                obs.page.cont.display(LoginPage)

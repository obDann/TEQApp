from Observer import Observer
import client_db_functions
from agency_page import *
from teq_page import *
from admin_page import *
from change_password_page import *

class LoginObserver(Observer):
    '''
    '''
    
    def __init__(self):
        ''' (LoginObserver) -> None
        
        Initializes a LoginObserver object
        '''

    def notify(self, obs):
        ''' (LoginObserver, Observable) -> None
        
        If all values are filled and correct, logs in
        the appropriate user
        '''
        username = obs.button.e1.get().lower()
        pw = obs.button.e2.get()

        if (username != "" and pw != ""):
            # checks if the user is using their temporary passcode first
            check_temp = client_db_functions.check_temp_pass(username, pw)
            if (check_temp[0] and check_temp[1]):
                obs.page.cont.set_page(ChangePasswordPage, username)
            elif (check_temp[0] and not check_temp[1]):
                (name, acc) = client_db_functions.login(username, pw)
                if (name != None and acc != None):
                    obs.page.cont.set_page(ChangePasswordPage, username)
            else:
                # grabs name and type of acc if login was successful
                (name, acc) = client_db_functions.login(username, pw)
                if (name != None and acc != None):
                    if (acc == "Agency"):
                        obs.page.cont.set_page(AgencyPage, name)
                    elif (acc == "TEQ"):
                        obs.page.cont.set_page(TEQPage, name)
                    else:
                        obs.page.cont.set_page(AdminPage, name)

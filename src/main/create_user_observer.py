from Observer import Observer
import client_db_functions
import main_page as mp

class CreateUserObserver(Observer):
    '''
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
        print("got notified")
        username = obs.button.e1.get()
        name = obs.button.e2.get()
        pw = obs.button.e3.get()
        acc = obs.button.acc.get()
    
        if (username != "" and name != "" and pw != ""):
            client_db_functions.insert_user(username, name, pw, acc)
            obs.page.cont.display(mp.MainPage)

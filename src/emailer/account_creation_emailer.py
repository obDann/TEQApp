from emailer import Emailer

class AccountCreationEmailer(Emailer):

    def __init__(self, email):
        '''
        (AccountCreationEmailer, str) -> None
        
        Initialize AccountCreationEmailer
        '''
        self.email = email

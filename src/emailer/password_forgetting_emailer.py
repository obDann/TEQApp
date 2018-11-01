from emailer import Emailer

class PasswordForgettingEmailer(Emailer):

    def __init__(self, email):
        '''
        (PasswordForgettingEmailer, str) -> None
        
        Initialize PasswordForgettingEmailer
        '''
        self.email = email

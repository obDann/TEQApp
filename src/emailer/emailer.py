from abc import ABC, abstractmethod

class Emailer(ABC):
    '''
    Sends emails accordingly
    '''

    def __init__ (self, email):
        '''
        (Emailer) -> None
        
        Intializes with an email address to use to send out other emails
        '''
        self.email = email

    @abstractmethod
    def send(self):
        '''
        (Emailer) -> None
        
        Sends an email
        '''

    @abstractmethod
    def sent_properly(self):
        '''
        (Emailer) -> boolean

        Returns a boolean to determine whether the email could be sent or not
        '''

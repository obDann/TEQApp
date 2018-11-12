from abc import ABC, abstractmethod

class Emailer(ABC):
    '''
    Sends emails accordingly
    '''

    def __init__ (self):
        '''
        (Emailer) -> None
        
        Intializes with an email address to use to send out other emails
        '''

    @abstractmethod
    def send(self):
        '''
        (Emailer) -> None
        
        Sends an email
	'''

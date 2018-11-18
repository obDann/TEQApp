from abc import ABC, abstractmethod

class Observer(ABC):
    '''
    Abstract Object that can be notified by observables
    '''
    
    @abstractmethod
    def notify(self, obs):
        ''' (Observer, Observable) -> Abstract
        
        Is notified of an event from the Observable
        '''

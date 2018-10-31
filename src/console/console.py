from abc import ABC, abstractmethod

class Console(ABC):
    '''
    An abstract representation of a console
    '''

    @abstractmethod
    def run_console(self):
        '''
        (Console) -> None

        Runs the console
        '''

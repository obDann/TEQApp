from abc import ABC, abstractmethod

'''Import OutputQueue'''
import sys
sys.path.insert(0, "../output")
from output_queue import *


class Command(ABC):
    '''
    A command that can be executed
    '''

    def __init__(self):
        '''
        (Command) -> None

        Initializes a Command
        '''
        # make an output queue
        self._opq = OutputQueue()
        # and make an execution status, be default, it will be false
        self._exec_status = False

    @abstractmethod
    def execute(self):
        '''
        (Command) -> Abstract

        Executes the command
        '''

    @abstractmethod
    def executed_properly(self):
        '''
        (Command) -> boolean

        Returns a boolean to determine if this command was executed properly
        '''

    def get_output_queue(self):
        '''
        (Command) -> OutputQueue

        Returns an OutputQueue
        '''
        return self._opq

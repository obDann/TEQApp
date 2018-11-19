import numpy as np
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod

class ReportAbstract(ABC):
    '''
    Abstract Class for report graphs
    '''
    
    def __init__(self, title, x_label, y_label):
        ''' (ReportAbstract, str, str, str) -> None
        
        Initialize a report
        Sets the title and axis labels
        These persist after a  display
        '''
        fig, ax = plt.subplots()
        self.title = title
        self.x_label = x_label
        self.y_label = y_label

    @abstractmethod
    def add_data(self):
        ''' (ReportAbstract) -> None
        
        Adds a dataset to the Report
        After a display, all data must be readded
        '''
        pass

    def display(self):
        ''' (ReportAbstract) -> None
        
        Displays a Report
        All added datasets will be reset
        '''
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.title(self.title)
        plt.legend()
        plt.show()

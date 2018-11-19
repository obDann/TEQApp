import numpy as np
import matplotlib.pyplot as plt
from report_abstract import ReportAbstract

class Histogram(ReportAbstract):
    '''
    Report object to display a histogram
    '''
    
    def __init__(self, title, x_label, y_label):
        ''' (Histogram, str, str, str) -> None
        
        Initializes a Histogram object
        Sets the title and axis labels
        These persist after a  display
        '''
        ReportAbstract.__init__(self, title, x_label, y_label)

    def add_data(self, x, x_label, x_color):
        ''' (Histogram, tuple of (int), str, str) -> None
        
        Adds a dataset to the Histogram
        x_color must be a single char representing the datas color
        such as "b" for blue or "g" for green.
        After a display, all data must be readded
        '''
        plt.hist(x,
                 color=x_color,
                 label=x_label)

    def display(self):
        ''' (Histogram) -> None
        
        Displays a Histogram
        All added datasets will be reset
        '''
        ReportAbstract.display(self)

if __name__ == "__main__":
    bg = Histogram("Scores", "Person", "Scores")
    bg.add_data((3, 3, 4, 4, 8, 7), "Frank", "b")
    bg.add_data((5, 5, 5, 6, 7, 7), "Guido", "g")
    bg.display()
    #bg.add_data((1, 2, 3, 4), (5, 5, 10, 8), "Frank", "b", "o")
    #bg.add_data((1, 2, 3, 4), (8, 4, 5, 6), "Guido", "g", "x")
    #bg.display()
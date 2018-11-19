import numpy as np
import matplotlib.pyplot as plt
from report_abstract import ReportAbstract

class ScatterPlot():
    '''
    Report object to display a ScatterPlot
    '''
    
    def __init__(self, title, x_label, y_label):
        ''' (ScatterPlot, str, str, str) -> None
        
        Initializes a ScatterPlot object
        Sets the title and axis labels
        These persist after a  display
        '''
        ReportAbstract.__init__(self, title, x_label, y_label)

    def add_data(self, x, y, x_label, x_color, marker):
        ''' (ScatterPlot, tuple of (int), tuple of (int), str, str, str) -> None
        
        Adds a dataset to the ScatterPlot
        x_color must be a single char representing the datas color
        such as "b" for blue or "g" for green.
        Marker should be 1 char representing the marker for the data set
        common markers are "x" and "o"
        After a display, all data must be readded
        '''
        plt.scatter(x, y,
                    c=x_color,
                    marker=marker,
                    label=x_label)

    def display(self):
        ''' (ScatterPlot) -> None
        
        Displays a ScatterPlot
        All added datasets will be reset
        '''
        ReportAbstract.display(self)

if __name__ == "__main__":
    bg = ScatterPlot("Scores per Day", "Person", "Scores")
    bg.add_data((1, 2, 3, 4), (5, 5, 10, 8), "Frank", "b", "o")
    bg.add_data((1, 2, 3, 4), (8, 4, 5, 6), "Guido", "g", "x")
    bg.display()
    bg.add_data((1, 2, 3, 4), (5, 5, 10, 8), "Frank", "b", "o")
    bg.add_data((1, 2, 3, 4), (8, 4, 5, 6), "Guido", "g", "x")
    bg.display()    
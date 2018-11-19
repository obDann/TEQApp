import numpy as np
import matplotlib.pyplot as plt
from report_abstract import ReportAbstract

class BarGraph(ReportAbstract):
    '''
    Report object to display a BarGraph
    '''
    
    def __init__(self, title, x_label, y_label, n_groups):
        ''' (BarGraph, str, str, str, int) -> None
        
        Initializes a bargraph object
        Sets the title, axis labels, and number of bars per data
        These persist after a  display
        '''
        ReportAbstract.__init__(self, title, x_label, y_label)
        self.n_groups = n_groups
        self.index = np.arange(self.n_groups)
        self.data = 0
        self.bar_width = 0.35
        self.opacity = 0.8

    def add_data(self, x, x_label, x_color):
        ''' (BarGraph, tuple of (int), str, str) -> None
        
        Adds a dataset to the BarGraph
        x_color must be a single char representing the datas color
        such as "b" for blue or "g" for green.
        After a display, all data must be readded
        '''
        plt.bar(self.index + self.data * self.bar_width, x, self.bar_width,
                alpha=self.opacity,
                color=x_color,
                label=x_label)
        self.data += 1

    def display(self, xticks):
        ''' (BarGraph, tuple of (str)) -> None
        
        Displays a BarGraph.
        xticks should have as many str as there are n_groups
        All added datasets will be reset
        '''
        plt.xticks(self.index + self.bar_width/2, xticks)
        ReportAbstract.display(self)

if __name__ == "__main__":
    while True:
        bg = BarGraph("Scores by Person", "Person", "Scores", 4)
        bg.add_data((90, 55, 40, 65), "Frank", "b")
        bg.add_data((85, 62, 54, 20), "Guido", "g")
        bg.display(('A', 'B', 'C', 'D'))
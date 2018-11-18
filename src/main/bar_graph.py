import numpy as np
import matplotlib.pyplot as plt

class BarGraph():
    '''
    Graph Object to display a BarGraph
    '''
    
    def __init__(self, title, x_label, y_label, n_groups):
        ''' (BarGraph, str, str, str, int) -> None
        
        Initializes a bargraph object
        Sets the title, axis labels, and number of bars per data
        '''
        fig, ax = plt.subplots()
        self.title = title
        self.x_label = x_label
        self.y_label = y_label
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
        '''
        plt.bar(self.index + self.data * self.bar_width, x, self.bar_width,
                alpha=self.opacity,
                color=x_color,
                label=x_label)
        self.data += 1

    def display(self, xticks):
        ''' (BarGraph, tuple of (str))
        
        Displays a BarGraph.
        xticks should have as many str as there are n_groups
        '''
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.title(self.title)
        plt.xticks(self.index + self.bar_width/2, xticks)
        plt.legend()
        plt.show()

if __name__ == "__main__":
    while True:
        bg = BarGraph("Scores by Person", "Person", "Scores", 4)
        bg.add_data((90, 55, 40, 65), "Frank", "b")
        bg.add_data((85, 62, 54, 20), "Guido", "g")
        bg.display(('A', 'B', 'C', 'D'))
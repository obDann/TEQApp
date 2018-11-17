import numpy as np
import matplotlib.pyplot as plt

class ScatterPlot():
    '''
    Graph Object to display a ScatterPlot
    '''
    
    def __init__(self, title, x_label, y_label):
        ''' (ScatterPlot, str, str, str) -> None
        
        Initializes a ScatterPlot object
        '''
        fig, ax = plt.subplots()
        self.title = title
        self.x_label = x_label
        self.y_label = y_label

    def add_data(self, x, y, x_label, x_color, marker):
        ''' (ScatterPlot, tuple of (int), str, str) -> None
        
        x_color must be a single char representing the datas color
        such as "b" for blue or "g" for green.
        '''
        plt.scatter(x, y,
                    c=x_color,
                    marker=marker,
                    label=x_label)

    def display(self):
        '''
        '''
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.title(self.title)
        plt.legend()
        plt.show()

if __name__ == "__main__":
    bg = ScatterPlot("Scores per Day", "Person", "Scores")
    bg.add_data((1, 2, 3, 4), (5, 5, 10, 8), "Frank", "b", "o")
    bg.add_data((1, 2, 3, 4), (8, 4, 5, 6), "Guido", "g", "x")
    bg.display()
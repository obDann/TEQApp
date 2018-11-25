import numpy as np
import matplotlib.pyplot as plt
from graph import Graph

width = 0.8

class Histogram(Graph):
    '''
    A simple histogram to be outputted to the user
    '''

    def __init__(self, df, x, y, title=None):
        ''' (ReportAbstract, DataFrame, str, str, str) -> None

        Given a DataFrame, a ranging variable label, frequency label that is in
        the dataframe, and an optional title, initialize a histogram
        '''
        # REPRESENTATION INVARIANT
        # Histogram is a Graph
        # self._x_label is a (sequential) quantitative variable in the
        # dataframe
        # self._y_label is a quantitative variable in the dataframe

        # just call an init
        Graph.__init__(self, df, x, y, title)


    def display(self, bins, hist_type):
        '''
        (ReportAbstract) -> None

        Displays a graph that a user can interact with
        '''
        self._check_axis_labels()
        plt.hist(self._df[self._x_label], bins, histtype=hist_type, 
                 rwidth=width)
        plt.title(self._title)
        plt.xlabel(self._x_label)
        plt.ylabel(self._y_label)
        plt.show()

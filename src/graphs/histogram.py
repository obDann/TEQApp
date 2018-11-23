import numpy as np
import matplotlib.pyplot as plt
from graph import Graph

class Histogram(Graph):
    '''
    A simple histogram to be outputted to the user
    '''

    def __init__(self, df, ranging_variable, frequency, title=None):
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
        Graph.__init__(self, df, ranging_variable, frequency, title)


    def display(self):
        '''
        (ReportAbstract) -> None

        Displays a graph that a user can interact with
        '''

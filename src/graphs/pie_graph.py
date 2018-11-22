import numpy as np
import matplotlib.pyplot as plt
from graph import Graph

class PieGraph(Graph):
    '''
    A simple pie graph to be outputted to the user
    '''

    def __init__(self, df, label, frequency, title=None):
        ''' (ReportAbstract, DataFrame, str, str, str) -> None

        Given a DataFrame, a column full of labels, a column of frequencies,
        and an optional title, initialize a pie graph.
        '''
        # REPRESENTATION INVARIANT
        # PieGraph is a Graph
        # self._x_axis is a categorial variable in the dataframe
        # self._y_axis is a quantitative variable in the dataframe

        # just call an init
        Graph.__init__(self, df, label, frequency, title)


    def display(self):
        '''
        (ReportAbstract) -> None

        Displays a graph that a user can interact with
        '''

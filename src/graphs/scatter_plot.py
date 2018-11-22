import numpy as np
import matplotlib.pyplot as plt
from graph import Graph

class ScatterPlot(Graph):
    '''
    A simple scatterplot to be outputted to the user
    '''

    def __init__(self, df, x_axis, y_axis, title=None):
        ''' (ReportAbstract, DataFrame, str, str, str) -> None

        Given a DataFrame, an x-axis column name, y-axis column name,
        and an optional title, initialize a scatterplot.
        '''
        # REPRESENTATION INVARIANT
        # Scatterplot is a Graph
        # self._x_axis is a quantitative variable in the dataframe
        # self._y_axis is a quantitative variable in the dataframe

        # just call an init
        Graph.__init__(self, df, x_axis, y_axis, title)


    def display(self):
        '''
        (ReportAbstract) -> None

        Displays a graph that a user can interact with
        '''

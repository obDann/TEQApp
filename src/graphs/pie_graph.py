import numpy as np
import matplotlib.pyplot as plt
from graph import Graph

group1 = 0
group2 = 0.15

class PieGraph(Graph):
    '''
    A simple pie graph to be outputted to the user
    '''

    def __init__(self, df, index, freq, title=None):
        ''' (ReportAbstract, DataFrame, str, str, str) -> None

        Given a DataFrame, a column full of labels, a column of frequencies,
        and an optional title, initialize a pie graph.
        '''
        # REPRESENTATION INVARIANT
        # PieGraph is a Graph
        # self._x_label is a categorial variable in the dataframe
        # self._y_label is a quantitative variable in the dataframe

        # just call an init
        Graph.__init__(self, df, index, freq, title)


    def display(self):
        '''
        (ReportAbstract) -> None

        Displays a graph that a user can interact with
        '''
        self._check_axis_labels()
        plt.pie(self._df[self._y_label], labels=self._df[self._x_label], 
                explode=(group1, group2), autopct='%1.1f%%')
        plt.title(self._title)
        plt.show()        

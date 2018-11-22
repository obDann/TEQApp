import numpy as np
import matplotlib.pyplot as plt
from label_not_in_data_frame_error import *
from abc import ABC, abstractmethod

class Graph(ABC):
    '''
    Abstract for graphs
    '''

    def __init__(self, df, x_axis, y_axis=None, title=None):
        ''' (Graph, DataFrame, str, str, str) -> None

        Given a DataFrame, an x label, a y label, and an optional
        title, initialize a graph.

        RAISES LabelNotInDataFrameError if the x axis or the y axis is not
        in the dataframe
        '''
        # REPRESENTATION INVARIANT
        # self._df is a dataframe
        # self._x_label and self._y_label are columns that are in the dataframe
        # self._title is the title of the graph
        fig, ax = plt.subplots()
        self._df = df
        self._x_label = x_label
        self._y_label = y_label
        self._title = title


    @abstractmethod
    def display(self):
        '''
        (Graph) -> None

        Displays a graph that a user can interact with
        '''

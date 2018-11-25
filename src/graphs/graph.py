import numpy as np
import matplotlib.pyplot as plt
from label_not_in_data_frame_error import LabelNotInDataFrameError
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
        self._x_label = x_axis
        self._y_label = y_axis
        self._title = title


    @abstractmethod
    def display(self):
        '''
        (Graph) -> None

        Displays a graph that a user can interact with
        '''

    def _check_axis_labels(self):
        '''
        (self) -> None

        Determines of the axis labels are in the dataframe

        RAISES LabelNotInDataFrameError if the x axis or the y axis is not
        in the dataframe
        '''
        # check if the x axis is in the data frame

        if (self._x_label not in self._df.columns):
            # if it isn't columns, then we raise an error
            msg = "The axis " + str(self._x_label) + " is not in the dataframe"
            raise LabelNotInDataFrameError(msg)
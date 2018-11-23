from predictive_model import *
import pandas as pd
from scipy import stats
import numpy as np

class NaiveModel(PredictiveModel):
    '''
    A model that is typically used when forecasts are stable
    '''

    def __init__(self, dataframe, x_axis, y_axis):
        '''
        (PredictiveModel, DataFrame, str, str) -> None

        Initializes a naive model predictive model.
        '''
        # run predictive model's init
        PredictiveModel.__init__(self, dataframe, x_axis, y_axis)


    def get_model(self, until=None):
        '''
        (PredictiveModel) -> (Dataframe, str)

        Returns the originally injected DataFrame with an extra column. The
        column name is the string in the tuple returned.

        The 'until' variable indicates how many entries there are in the
        data to predict
        '''

        # the Naive approach is to just simply get the first entry in the
        # y-axis and call it a day
        first_entry = self._df[self._y_axis][0]
        # set the dataframe
        new_col = "Naive Model"
        self._df.loc[:, new_col] = first_entry
        # then return the Naive model
        return self._df, new_col

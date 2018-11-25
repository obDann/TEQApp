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


    def get_model(self, until=None, increment_by=1.0):
        '''
        (PredictiveModel, float, float) -> (Dataframe, str)

        Returns the a DataFrame of the passed x, y, and an extra column.
        The column name is the string in the tuple returned that indicates
        where the predictive model lies.

        'until' is the x-axis limit

        The 'increment_by' variable indicates how the x axis will be
        incrementing.
        '''
        x_axis_col = self._handle_until(until, increment_by)
        # then set the dataframe
        new_df = pd.DataFrame(x_axis_col)

        # insert the y axis
        new_df.loc[:, self._y_axis] = self._df[self._y_axis]

        # the Naive approach is to just simply get the first entry in the
        # y-axis and call it a day
        first_entry = self._df[self._y_axis][0]
        # set the dataframe
        new_col = "Naive Model"
        new_df.loc[:, new_col] = first_entry

        # then return the Naive model
        return new_df, new_col

from predictive_model import *
import pandas as pd
from scipy import stats
import numpy as np


class LinearRegressionModel(PredictiveModel):
    '''
    A predictive model that uses linear regression
    '''

    def __init__(self, dataframe, x_axis, y_axis):
        '''
        (PredictiveModel, DataFrame, str, str) -> None

        Initializes a linear regression model
        '''
        PredictiveModel.__init__(self, dataframe, x_axis, y_axis)
        self._x_coeff = None
        self._y_coeff = None


    def get_model(self, until=None, increment_by=1):
        '''
        (PredictiveModel, float, float) -> (Dataframe, str)

        Returns the a DataFrame of the passed x, y, and an extra column.
        The column name is the string in the tuple returned that indicates
        where the predictive model lies.

        'until' is the x-axis limit

        The 'increment_by' variable indicates how the x axis will be
        incrementing.
        '''
        # first, get the x coefficient and the y-intercept respectively
        coeff, y_int = self.get_details()
        # then, let's handle the "until" thing
        base_df = pd.DataFrame(self._handle_until(until, increment_by))
        # set the y axis
        base_df.loc[:, self._y_axis] = self._df[self._y_axis]
        # then we want to make a new dataframe
        predict = coeff * base_df[self._x_axis] + y_int
        column = "Linear Regression"
        base_df.loc[:, column] = predict
        return base_df, column


    def get_details(self):
        '''
        (PredictiveModel) -> tuple of (float, float)

        Returns the x coefficient and the y-intercept respectively
        '''
        # we get our x values
        x_vals = self._df[self._x_axis]
        y_vals = self._df[self._y_axis]

        # we want to make the coefficient, the numerator is
        # \Sum (x_i * y_i) - n * avg(x) * avg(y)
        numerator = x_vals * y_vals
        numerator = numerator.sum()
        numerator -= self._num_entries * x_vals.mean() * y_vals.mean()
        # we want to get the denominator, which is
        # \Sum (x_i)^2 - n * avg(x) ^2
        denominator = x_vals**2
        denominator = denominator.sum()
        denominator -= self._num_entries * x_vals.mean()**2
        coefficient = numerator / denominator

        # we want to get the y-intercept which is
        # intercept = avg(y) - coefficient * avg(x)
        y_intercept = y_vals.mean() - coefficient * x_vals.mean()
        # then return as expected
        return coefficient, y_intercept

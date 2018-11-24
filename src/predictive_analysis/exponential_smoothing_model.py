from predictive_model import *
import pandas as pd
from scipy.optimize import minimize
import numpy as np


class ExponentialSmoothingModel(PredictiveModel):
    '''
    A predictive model that uses exponential smoothing
    '''
    BEST_GUESS = 0.5

    def __init__(self, dataframe, x_axis, y_axis):
        '''
        (PredictiveModel, DataFrame, str, str) -> None

        Initializes an exponential smoothing model. The dataframe's x-axis
        must only increment by 1
        '''
        # just initialize the model
        PredictiveModel.__init__(self, dataframe, x_axis, y_axis)

    def get_model(self, until=None, increment_by=1.0):
        '''
        (PredictiveModel, float, float) -> (Dataframe, str)

        Returns the originally injected DataFrame of only the x and y values.
        The column name is the string in the tuple returned.

        The model will only have 1 extra entry, thus "until" will not be used
        '''
        # we want to get the most optimal alpha
        alpha = self._get_optimal_alpha()

        # and then, we want to get our original model with an afiliated list
        base_model, col = self._make_smoothing_model_for_optimizing(alpha)
        # we're of interest in the last y value and forecast value
        last_x_val = float(base_model.tail(1)[self._x_axis])
        last_y_val = float(base_model.tail(1)[self._y_axis])
        prev_for_val = float(base_model.tail(1)[col])

        # then we want to add one last forecast value
        last_forecast_val = prev_for_val + alpha * (last_y_val - prev_for_val)

        # then we want to make a simple dataframe
        cols = [self._x_axis, self._y_axis, col]
        new_df = pd.DataFrame([[last_x_val + increment_by, 0,
                                last_forecast_val]], columns=cols)
        base_model = base_model.append(new_df)

        # we would want to reset the index
        base_model.reset_index(drop=True)
        return base_model, col

    def _get_optimal_alpha(self):
        '''
        (PredictiveModel) -> float

        Returns the optimal alpha for the model
        '''
        # the objective is to minimize the _test_alpha function
        # we have our best guess at the top so
        x0 = [self.BEST_GUESS]

        # bounds is just 0 to 1
        b = ((0, 1))
        # relatively no other constraints; we will use simplex method
        sol = minimize(self._test_alpha, x0, method='Nelder-Mead', bounds=b)
        return sol.x[0]

    def _test_alpha(self, alpha):
        '''
        (PredictiveModel, float) -> double

        Returns the MAPE for the alpha value passed
        '''
        # get the dataframe of our alpha
        the_df, col = self._make_smoothing_model_for_optimizing(alpha)
        # return the MAPE
        return self.get_mape_estimate(the_df, col)

    def _make_smoothing_model_for_optimizing(self, alpha):
        '''
        (PredictiveModel, float) -> tuple of (DataFrame, str)

        Given an alpha, return a smoothing model
        '''
        # what we want to do is to make a dataframe that only has x, y and
        # the upcoming dataframe
        my_df = pd.DataFrame(self._df[self._x_axis])
        my_df.loc[:, self._y_axis] = self._df[self._y_axis]
        # let's reset the index to 0
        my_df.reset_index(drop=True)

        # create a model and an n-1 actual
        model = []
        previous_actual = None
        # and now we can go through the data frame
        for index, x, y in my_df.itertuples():
            # the base case of this model is that the first entry should
            # be the y value
            if (index == 0):
                model.append(y)
                previous_actual = y
            # otherwise, our new entry is going to be
            # Forecast_{t-1} + \alpha * (Actual_{t-1} - Forecast_{t-1})
            else:
                # previous forecast
                prev_for = model[index - 1]
                forecast_val = prev_for + alpha * (previous_actual - prev_for)
                # then append the forecast value
                model.append(forecast_val)
                # and then set a new actual value
                previous_actual = y
        # now we want to create a dataframe with our model
        label = "Exponential Smoothing Non Trending"
        modeled_df = pd.DataFrame({label: model})
        # then append the model to our df
        my_df.loc[:, label] = modeled_df
        return my_df, label

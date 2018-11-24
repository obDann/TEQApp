from predictive_model import *
import pandas as pd
from scipy.optimize import minimize
import numpy as np


class ExponentialSmoothingTrendsModel(PredictiveModel):
    '''
    A predictive model that uses exponential smoothing with trending factor
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
        # and we need the last trend factor
        self._trend_factor = None
        self._smooth = None

    def get_model(self, until=None, increment_by=1.0):
        '''
        (PredictiveModel, float, float) -> (Dataframe, str)

        Returns the a DataFrame of the passed x, y, and an extra column.
        The column name is the string in the tuple returned that indicates
        where the predictive model lies.

        The model will only have 1 extra entry, thus "until" will not be used
        '''
        # we want to get the most optimal alpha
        alpha, beta = self.get_optimal_alpha_and_beta()
        # and then, we want to get our original model with an afiliated list
        base_model, col = self._make_trends_model(alpha, beta)
        # we're of interest in the last y value and forecast value
        last_x_val = float(base_model.tail(1)[self._x_axis])
        last_y_val = float(base_model.tail(1)[self._y_axis])
        prev_for_val = float(base_model.tail(1)[col])
        # then we want to add one last forecast value
        # following the forumla...
        # Smoothing_t = \alpha * Actual_{t-1}
        #               + (1 - \alpha) * (Smoothing_{t-1} + Trend_{t-1})
        # Trend_t = \beta * ((Smoothing_t) - Smoothing_{t-1})
        #           + (1 - \beta) * Trend_{t-1}
        smoothing = alpha * last_y_val
        smoothing += + (1 - alpha) * (self._smooth + self._trend_factor)
        trend = beta * (smoothing - self._smooth)
        trend += (1 - beta) * self._trend_factor
        last_forecast_val = smoothing + trend

        # then we want to make a simple dataframe
        cols = [self._x_axis, self._y_axis, col]
        new_df = pd.DataFrame([[last_x_val + increment_by, 0,
                                last_forecast_val]], columns=cols)
        base_model = base_model.append(new_df)
        # we would want to reset the index
        base_model.reset_index(drop=True)
        return base_model, col

    def get_optimal_alpha_and_beta(self):
        '''
        (PredictiveModel) -> float

        Returns the optimal alpha for the model
        '''
        # the objective is to minimize the _test_alpha function
        # we have our best guess at the top so
        x0 = [self.BEST_GUESS, self.BEST_GUESS]

        # bounds is just 0 to 1
        b = ((0, 1), (0, 1))
        # relatively no other constraints; we will use simplex method
        sol = minimize(self._test_alpha_and_beta, x0, method='Nelder-Mead',
                       bounds=b)
        return sol.x[0], sol.x[1]

    def _test_alpha_and_beta(self, vector):
        '''
        (PredictiveModel, list of floats) -> double

        Returns the MAPE for the alpha and beta value passed in the vector
        '''
        alpha = vector[0]
        beta = vector[1]
        # get the dataframe of our alpha
        the_df, col = self._make_trends_model(alpha, beta)
        # return the MAPE
        return self.get_mape_estimate(the_df, col)

    def _make_trends_model(self, alpha, beta):
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
        # create a model, n-1 actual, and n-1 trend
        model = []
        previous_actual = None
        previous_trend = 0
        previous_smoothing = None
        # and now we can go through the data frame
        for index, x, y in my_df.itertuples():
            # the base case of this model is that the first entry should
            # be the y value
            if (index == 0):
                model.append(y)
                previous_actual = y
                previous_smoothing = y
            # otherwise, our new entry is going to be
            # Forecast_t = Smoothing_t + Trend_t
            # where
            #
            # Smoothing_t = \alpha * Actual_{t-1}
            #               + (1 - \alpha) * (Smoothing_{t-1} + Trend_{t-1})
            # Trend_t = \beta * ((Smoothing_t) - Smoothing_{t-1})
            #           + (1 - \beta) * Trend_{t-1}
            else:
                # previous forecast
                prev_for = model[index - 1]
                # create smoothing
                smooth = alpha * previous_actual
                smooth += (1 - alpha) * (previous_smoothing + previous_trend)
                # create trend
                trend = beta * (smooth - previous_smoothing)
                trend += (1 - beta) * previous_trend
                # then the forecast value is the sum of the smooth and trend
                forecast_val = smooth + trend
                # then append the forecast value
                model.append(forecast_val)
                # and then set a previous trend, smoothing value and smoothing
                previous_actual = y
                previous_trend = trend
                previous_smoothing = smooth
        # now we want to create a dataframe with our model
        label = "Exponential Smoothing With Trends"
        modeled_df = pd.DataFrame({label: model})
        # then append the model to our df
        my_df.loc[:, label] = modeled_df
        # set the last trending factor
        self._trend_factor = previous_trend
        self._smooth = previous_smoothing
        return my_df, label

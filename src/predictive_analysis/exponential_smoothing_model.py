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

        Returns the originally injected DataFrame with an extra column. The
        column name is the string in the tuple returned.

        'until' is the x-axis limit

        The 'increment_by' variable indicates how the x axis will be
        incrementing.
        '''

    def _get_optimal_alpha(self):
        '''
        (PredictiveModel) -> float

        Returns the optimal alpha for the model
        '''
        # the objective is to minimize the _test_alpha function
        # best representative data of an "initial guess" is our y values so
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
        my_df = pd.DataFrame({self._x_axis: list(self._df[self._x_axis])})
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
                prev_fore = model[index - 1]
                forecast_val = prev_fore + alpha * (previous_actual - prev_fore)
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




#x = "x axis"
#y = "y axis"
#the_data = {x: [i for i in range(1, 13)],
            #y: [6320, 6672, 6432, 6542, 6774, 6685, 6932, 6751, 6892, 7169,
                #7132, 7282]}
#the_df = pd.DataFrame(the_data)

##for index, x, y in the_df.itertuples():
    ##print("this is the index " + str(index))
    ##print("this is a x " + str(x))
    ##print("this is a y " + str(y))
#my_esm = ExponentialSmoothingModel(the_df, x, y)

#mape = my_esm._get_optimal_alpha()

from predictive_model import *
import pandas as pd
from scipy import stats
import numpy as np


class ExponentialSmoothingTrendModel(PredictiveModel):
    '''
    A predictive model that uses exponential smoothing with trending weights
    '''

    def __init__(self, dataframe, x_axis, y_axis):
        '''
        (PredictiveModel, DataFrame, str, str) -> None

        Initializes an exponential smoothing model with trends
        '''
        PredictiveModel.__init__(self)


    def get_model(self):
        '''
        (PredictiveModel) -> (Dataframe, str)

        Returns the originally injected DataFrame with an extra column. The
        column name is the string in the tuple returned.
        '''


    def get_MAPE(self):
        '''
        (PredictiveModel) -> float

        Returns the Mean Absolute Percent Error. The lower it is, the more
        accurate the model is in a long term basis.
        '''

    def _test_alpha_and_beta(self):
        '''
        (PredictiveModel) -> (double, double)

        Returns the optimal alpha and beta in the exponential smoothing model
        with trends.
        '''


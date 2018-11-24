from abc import ABC, abstractmethod
from bad_dataframe_error import *
import pandas as pd

class PredictiveModel(ABC):
    '''
    A generic predictive model
    '''

    def __init__(self, dataframe, x_axis, y_axis):
        '''
        (PredictiveModel, DataFrame, str, str) -> None

        Initializes a predictive model.

        RAISES BadDataFrameError if the dataframe is empty or if the x and
        y axis labels are not in the specified dataframe
        '''
        # REPRESENTATION INVARIANT

        # self._df is a copy of the dataframe that contains the data
        # self._x_axis is a string that is a column name in self._df
        # self._y_axis is a string that is a column name in self._df
        # self._df[self._x_axis] is a quantitative variable
        # self._df[self._y_axis] is a quantitative variable
        # there is at least one row in the dataframe
        # self._num_entries is the original number of entries in the dataframe

        # check if the dataframe is valid
        self._check_dataframe(dataframe, x_axis, y_axis)

        self._df = dataframe[:].dropna()
        self._x_axis = x_axis
        self._y_axis = y_axis
        self._num_entries = self._df.shape[0]


    @abstractmethod
    def get_model(self, until=None, increment_by=1.0):
        '''
        (PredictiveModel, int) -> (Dataframe, str)

        Returns the originally injected DataFrame with an extra column. The
        column name is the string in the tuple returned.

        The 'until' variable indicates how many entries there are in the
        data to predict
        '''

    def get_mape_estimate(self, mod=None, model_col=None):
        '''
        (PredictiveModel, DataFrame, str) -> float

        Returns the Mean Absolute Percent Error. The lower it is, the more
        accurate the model is in a long term basis. The formula used to
        create this mape estimate is

                     sum( |(Actual - Expected) / (|Actual| + 1)|)
                 ==================================================
                                         n

        the " + 1" in the formula is there in the event that the actual
        value is 0

        Optional parameters are provided in the event that the model is
        already made
        '''
        # check if the model is not created
        if (mod is None):
            # if not, get the model and the name
            mod, model_col = self.get_model()
        # in the event that they inject a model with more x-axis variables,
        # get the top n
        mod = mod.head(self._num_entries)[:]

        # we want to have a copy of the model so that the original one is not
        # mutated
        mod = mod.head(self._num_entries)[:]
        # what is wanted is to have an intermediate calculation for a new
        # column taking this off of MGOC20...
        inter_step = "An intermediate step to avoid bad things"
        # actual - forecast
        mod.loc[:, inter_step] = mod[self._y_axis] - mod[model_col]
        # (actual - forecast) / (|actual| + 1)
        # + 1 is used IN THE EVENT THAT ACTUAL IS 0
        mod[inter_step] = mod[inter_step] / (mod[self._y_axis].abs() + 1)
        # |(actual - forecast) / (actual + 1)|
        mod[inter_step] = mod[inter_step].abs()
        # sum |(actual - forecast) / (actual + 1)|
        another_intermediate = mod[inter_step].sum()
        # sum |(actual - forecast) / (actual + 1)|  / n
        return another_intermediate / self._num_entries

    def _check_dataframe(self, dataframe, x_axis, y_axis):
        '''
        (PredictiveModel, DataFrame, str, str) -> None

        Checks whether or not the initial dataframe arguments are valid;
        i.e. if the dataframe is empty or the x and y axis labels are not
        in the dataframe
        '''
        # drop any nas
        dataframe = dataframe.dropna()

        # check if the dataframe is empty
        if (dataframe.empty):
            # if it is, then we have to provide a message
            msg = "Cannot make a predictive model with an empty dataframe"
            raise BadDataFrameError(msg)

        # then check if the dataframe's x and y axis are in the dataframe
        if x_axis not in dataframe:
            msg = "'" + x_axis + "' is not in the dataframe passed"
            raise BadDataFrameError(msg)
        if y_axis not in dataframe:
            msg = "'" + y_axis + "' is not in the dataframe passed"
            raise BadDataFrameError(msg)

    def _handle_until(self, until, increment_by):
        '''
        (PredictiveModel, float, float) -> DataFrame

        Returns a base x axis dataframe
        '''
        # if until is None, then set we return the original x axis df
        if until is None:
            return self._df[self._x_axis]
        # otherwise
        # get the first row's x-axis value
        curr = float(self._df.head(1)[self._x_axis])
        # we can make a list as our x values
        my_x_list = []
        while curr < (until):
            my_x_list.append(curr)
            curr += increment_by
        x_axis_col = {self._x_axis: my_x_list}
        return x_axis_col

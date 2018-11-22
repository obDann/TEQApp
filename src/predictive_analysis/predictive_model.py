from abc import ABC, abstractmethod

class PredictiveModel(ABC):
    '''
    A generic predictive model
    '''

    def __init__(self, dataframe, x_axis, y_axis):
        '''
        (PredictiveModel, DataFrame, str, str) -> None

        Initializes a predictive model.
        '''
        self._df = dataframe
        self._x_axis = x_axis
        self._y_axis = y_axis


    @abstractmethod
    def get_model(self):
        '''
        (PredictiveModel) -> (Dataframe, str)

        Returns the originally injected DataFrame with an extra column. The
        column name is the string in the tuple returned.
        '''

    @abstractmethod
    def get_MAPE(self):
        '''
        (PredictiveModel) -> float

        Returns the Mean Absolute Percent Error. The lower it is, the more
        accurate the model is in a long term basis.
        '''

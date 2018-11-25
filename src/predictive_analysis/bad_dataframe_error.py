class BadDataFrameError(Exception):
    '''
    An exception when the dataframe passed is bad

    i.e. it is an empty dataframe or its labels are not in the dataframe
    '''

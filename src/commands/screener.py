import sys
from command import Command
import pandas as pd
sys.path.append("../temhelp")
from true_tem_handler import TrueTemplateHandler
sys.path.append("../output")
from output_queue import *


class Screener(Command):
    '''
    A Command that determines whether or not the dataframe
    from the excel file format is consistent with the iCare templates
    '''

    def __init__(self, df, template_handler):
        '''
        (Screener, DataFrame, TemplateHandler) -> None

        Initializes a Screener
        '''
        Command.__init__(self)
        # copy the dataframe (in the event of mutation)
        self._df = df[:]
        self._th = template_handler

    def execute(self):
        '''
        (Screener) -> DataFrame

        Determines if the dataframe is consistent with the excel file. If
        there is inconsistencies, then this method will return an empty
        dataframe, and its excution status will stay false
        '''
        # check if there are at least 2 rows
        num_rows = len(self._df.index)
        if (num_rows < 2):
            self._exec_status = False
            return pd.DataFame()
        # otherwise, we can assume that there are at least 3 rows

        # we are going to be appropriately setting the headers. The
        # headers are typically on the third row. The title is in the
        # 1st row, so the headers are actually on the 3rd row.
        header = self._df.iloc[1]
        headers_list = list(header)

        # use the template handler to get the template headers
        the_headers = self._th.get_headers()

        # check if the headers from the template is different from the headers
        # list

        if (headers_list != the_headers):
            # set the execution status to false
            self._exec_status = False
            # if they are not the same, return an empty dataframe
            return pd.DataFrame()

        # otherwise, we can assume that they are the same
        self._exec_status = True

        # cut the rest of the dataframe
        self._df = self._df[2:]
        # and then rename the headers
        self._df = self._df.rename(columns=header)

        # then return the dataframe while resetting the index
        return self._df.reset_index(drop=True)

    def executed_properly(self):
        '''
        (Screener) -> bool

        Returns a boolean to determine if this command was executed properly
        '''
        return self._exec_status

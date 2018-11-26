import sys
import unittest

import pandas as pd
'''Import duplicate row checker'''
sys.path.insert(0, "../commands")
from duplicate_row_checker import *


class TestDuplicateRowCheck(unittest.TestCase):

    def test_empty_dataframe(self):
        # make a dataframe
        my_df = pd.DataFrame()
        # make a duplicate row check
        my_drc = DuplicateRowChecker(my_df)
        # get the dataframe after excution
        actual = my_drc.execute()
        # test the two
        self.assertTrue(my_df.equals(actual))

        # and check our execution status
        self.assertTrue(my_drc.executed_properly())

    def test_non_duplicate_dataframe(self):
        # set up a dataframe
        set_up = {"first_col": [i for i in range(5)],
                  "second_col": [i for i in range(5)]}
        my_df = pd.DataFrame(set_up)

        # inject the dataframe into a drc
        my_drc = DuplicateRowChecker(my_df)
        # get the dataframe after excution
        actual = my_drc.execute()
        # test the two
        self.assertTrue(my_df.equals(actual))

        # and check our execution status
        self.assertTrue(my_drc.executed_properly())

    def test_duplicate_dataframe(self):
        # set up a dataframe
        set_up = {"first_col": [i for i in range(5)] + [i for i in range(5)],
                  "second_col": [i for i in range(5)] + [i for i in range(5)]}
        inject = pd.DataFrame(set_up)

        # inject the dataframe into a drc
        my_drc = DuplicateRowChecker(inject)
        # get the dataframe after excution
        actual = my_drc.execute()

        # make an expected dataframe
        set_up = {"first_col": [i for i in range(5)],
                  "second_col": [i for i in range(5)]}
        my_df = pd.DataFrame(set_up)

        # test the two
        self.assertTrue(my_df.equals(actual))

        # and check our execution status
        self.assertTrue(my_drc.executed_properly())


if __name__ == '__main__':
    unittest.main(exit=False)

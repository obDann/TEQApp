import sys
import unittest

import pandas as pd
'''Template handler'''
sys.path.append("../../temhelp")
from true_tem_handler import TrueTemplateHandler
'''OutputQueue'''
sys.path.append("../../output")
'''Import screener'''
sys.path.append("../../commands")
from screener import *


class TestScreener(unittest.TestCase):

    def test_sample_excelfile(self):
        my_df = pd.read_excel('client_exit_example.xlsx')
        headers = list(my_df.iloc[1])
        example_data = list(my_df.iloc[2])
        expected_df = pd.DataFrame([example_data], columns=headers)

        # make a TrueTemplateHandler
        my_tth = TrueTemplateHandler("Language Training - Client Exit")
        # make a screener
        my_screener = Screener(my_df, my_tth)
        actual_df = my_screener.execute()

        self.assertTrue(actual_df.iloc[0].equals(expected_df.iloc[0]))
        self.assertTrue(my_screener.executed_properly())

    def test_not_specified_template(self):
        my_df = pd.read_excel('empty_employment.xlsx')

        expected_df = pd.DataFrame()

        # make a TrueTemplateHandler
        my_tth = TrueTemplateHandler("Community Connections")
        # make a screener
        my_screener = Screener(my_df, my_tth)
        actual_df = my_screener.execute()

        self.assertTrue(expected_df.equals(actual_df))
        self.assertFalse(my_screener.executed_properly())

    def test_empty_row_template(self):
        my_df = pd.read_excel('empty_employment.xlsx')
        headers = list(my_df.iloc[1])
        expected_df = pd.DataFrame(columns=headers)

        # make a TrueTemplateHandler
        my_tth = TrueTemplateHandler("Employment Related Services")
        # make a screener
        my_screener = Screener(my_df, my_tth)
        actual_df = my_screener.execute()

        # then test the two
        self.assertTrue(actual_df.equals(expected_df))
        self.assertTrue(my_screener.executed_properly())


if __name__ == '__main__':
    unittest.main(exit=False)

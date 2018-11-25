import sys
import unittest

import pandas as pd
'''Predictive Analysis'''
sys.path.append("../../predictive_analysis")
from naive_model import *


class TestNaiveModel(unittest.TestCase):

    def setUp(self):
        x = "x axis"
        y = "y axis"
        the_data = {x: [i for i in range(15)],
                    y: [3, 5, 1, 6, 8, 4, 7, 3, 1, 8, 5, 4, 7, 3, 6]}
        the_df = pd.DataFrame(the_data)
        self.naive_first = NaiveModel(the_df, x, y)

        data_with_zero = {x: [i for i in range(5)],
                          y: [1, 0, 2, -1, -4]}
        df_zero = pd.DataFrame(data_with_zero)
        self.naive_second = NaiveModel(df_zero, x, y)

    def test_col_name_returned(self):
        dummy, actual = self.naive_first.get_model()
        expected = "Naive Model"
        self.assertEqual(actual, expected)

    def test_col_is_naive(self):
        the_df, the_col_name = self.naive_first.get_model()
        actual_first_naive = list(the_df[the_col_name])
        expected = [3 for i in range(15)]
        self.assertEqual(actual_first_naive, expected)

    def test_col_is_naive_pt_two(self):
        the_df, the_col_name = self.naive_second.get_model()
        actual_second_naive = list(the_df[the_col_name])
        expected = [1 for i in range(5)]
        self.assertEqual(actual_second_naive, expected)

    def test_naive_mape_estimate(self):
        actual = self.naive_first.get_mape_estimate()
        expected = 0.4023280423280423
        self.assertEqual(actual, expected)

    def test_naive_mape_estimate_pt_two(self):
        actual = self.naive_second.get_mape_estimate()
        expected = 0.6666666666666666
        self.assertEqual(actual, expected)

    def test_optional_params_big_n(self):
        big_n = 50
        x = "x axis"
        my_model, col = self.naive_first.get_model(big_n)

        # we expect that there are are 50 rows
        actual_num_rows = my_model.shape[0]
        self.assertEqual(actual_num_rows, big_n)

        # we expect that there is a column full of 3s indicated by the column
        naive_predict = {x: [3 for i in range(50)]}
        expected_df = pd.DataFrame(naive_predict)
        actual_predict = my_model[col]

        self.assertTrue(actual_predict.equals(expected_df[x]))

    def test_optional_params_mape(self):
        my_model, col = self.naive_first.get_model(20, 1)
        actual = self.naive_first.get_mape_estimate(my_model, col)
        expected = 0.4023280423280423
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(exit=False)

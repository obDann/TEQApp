import sys
import unittest

import pandas as pd
'''Predictive Analysis'''
sys.path.append("../../predictive_analysis")
from exponential_smoothing_trends_model import *


class TestExponentialSmoothingTrendModel(unittest.TestCase):

    def setUp(self):
        x = "x axis"
        y = "y axis"
        the_data = {x: [i for i in range(1, 13)],
                    y: [6320, 6672, 6432, 6542, 6774, 6685, 6932, 6751, 6892,
                        7169, 7132, 7282]}
        the_df = pd.DataFrame(the_data)
        self.my_estm = ExponentialSmoothingTrendsModel(the_df, x, y)
        self.model, self.col = self.my_estm.get_model()

    def test_optimal_alpha_and_beta(self):
        actual_alpha, actual_beta = self.my_estm.get_optimal_alpha_and_beta()
        expected_alpha = 0.17032329518980965
        expected_beta = 0.8682335143306051
        self.assertEqual(actual_alpha, expected_alpha)
        self.assertEqual(actual_beta, expected_beta)

    def test_size_of_model(self):
        # we expect that the model will of size 13, because it will have
        # one extra entry
        actual_num_rows = self.model.shape[0]
        expected_num_rows = 13
        self.assertEqual(actual_num_rows, expected_num_rows)

    def test_prediction(self):
        expected_prediction = [6320.0, 6320.0, 6432.007698297378,
                               6484.0591470613235, 6554.548900135578,
                               6685.000125599396, 6778.0736766350865,
                               6920.127172891355, 6982.1465403222965,
                               7044.28724352415, 7161.466061617923,
                               7248.027182588704, 7350.417336074257]
        actual_prediction = list(self.model[self.col])
        self.assertEqual(expected_prediction, actual_prediction)

    def test_big_n_does_not_matter(self):
        actual, col = self.my_estm.get_model(500, 1)
        self.assertTrue(actual[col].equals(self.model[self.col]))

    def test_mape_estimate(self):
        expected = 0.015042961355131607
        actual = self.my_estm.get_mape_estimate(self.model, self.col)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(exit=False)

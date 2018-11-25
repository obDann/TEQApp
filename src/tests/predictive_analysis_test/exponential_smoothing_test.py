import sys
import unittest

import pandas as pd
'''Predictive Analysis'''
sys.path.append("../../predictive_analysis")
from exponential_smoothing_model import *


class TestExponentialSmoothingModel(unittest.TestCase):

    def setUp(self):
        x = "x axis"
        y = "y axis"
        the_data = {x: [i for i in range(1, 13)],
                    y: [6320, 6672, 6432, 6542, 6774, 6685, 6932, 6751, 6892,
                        7169, 7132, 7282]}
        the_df = pd.DataFrame(the_data)
        self.my_esm = ExponentialSmoothingModel(the_df, x, y)
        self.model, self.col = self.my_esm.get_model()

    def test_optimal_alpha(self):
        actual_alpha = self.my_esm.get_optimal_alpha()
        expected_alpha = 0.6524414062500005
        self.assertEqual(actual_alpha, expected_alpha)

    def test_size_of_model(self):
        # we expect that the model will of size 13, because it will have
        # one extra entry
        actual_num_rows = self.model.shape[0]
        expected_num_rows = 13
        self.assertEqual(actual_num_rows, expected_num_rows)

    def test_prediction(self):
        expected_prediction = [6320.0, 6320.0, 6549.659375, 6472.893526916504,
                               6517.981451396078, 6685.018553273305,
                               6685.006448349579, 6846.155268523062,
                               6784.072031315779, 6854.488706977818,
                               7059.6888972787165, 7106.867654825679,
                               7221.131248391073]
        actual_prediction = list(self.model[self.col])
        self.assertEqual(expected_prediction, actual_prediction)

    def test_big_n_does_not_matter(self):
        actual, col = self.my_esm.get_model(500, 1)
        self.assertTrue(actual[col].equals(self.model[self.col]))

    def test_mape_estimate(self):
        expected = 0.021901559589262393
        actual = self.my_esm.get_mape_estimate(self.model, self.col)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(exit=False)

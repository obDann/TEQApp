import sys
import unittest

import pandas as pd
'''Predictive Analysis'''
sys.path.append("../../predictive_analysis")
from linear_regression_model import *


class TestLinearRegression(unittest.TestCase):

    def setUp(self):
        x = "x axis"
        y = "y axis"
        the_data = {x: [i for i in range(1, 13)],
                    y: [6320, 6672, 6432, 6542, 6774, 6685, 6932, 6751, 6892,
                        7169, 7132, 7282]}
        the_df = pd.DataFrame(the_data)
        self.lin_reg = LinearRegressionModel(the_df, x, y)
        self.model, self.col = self.lin_reg.get_model()

    def test_get_details(self):
        actual_coeff, actual_inter = self.lin_reg.get_details()
        expected_coeff = 76.25524475524476
        expected_inter = 6302.924242424242
        self.assertEqual(actual_coeff, expected_coeff)
        self.assertEqual(actual_inter, expected_inter)

    def test_get_mape_estimate(self):
        expected_mape = 0.014030043424653582
        actual_mape = self.lin_reg.get_mape_estimate()
        self.assertEqual(actual_mape, expected_mape)

    def test_the_linear_reg(self):
        expected_entries = [6379.179487179486, 6455.434731934732,
                            6531.689976689976, 6607.945221445221,
                            6684.200466200466, 6760.455710955711,
                            6836.710955710955, 6912.9662004662005,
                            6989.221445221445, 7065.476689976689,
                            7141.731934731934, 7217.98717948718]
        actual_entries = list(self.model[self.col])
        self.assertEqual(actual_entries, expected_entries)

    def test_n_many(self):
        expected_entries = [6379.179487179486, 6455.434731934732,
                            6531.689976689976, 6607.945221445221,
                            6684.200466200466, 6760.455710955711,
                            6836.710955710955, 6912.9662004662005,
                            6989.221445221445, 7065.476689976689,
                            7141.731934731934, 7217.98717948718,
                            7294.242424242424, 7370.497668997668,
                            7446.752913752914, 7523.008158508158,
                            7599.263403263403, 7675.518648018648,
                            7751.773892773892, 7828.029137529137,
                            7904.284382284382, 7980.539627039627,
                            8056.794871794871, 8133.050116550116,
                            8209.305361305362, 8285.560606060606,
                            8361.81585081585, 8438.071095571095,
                            8514.32634032634]
        new_model, the_col = self.lin_reg.get_model(30)
        actual_entries = list(new_model[the_col])
        self.assertEqual(expected_entries, actual_entries)

if __name__ == '__main__':
    unittest.main(exit=False)

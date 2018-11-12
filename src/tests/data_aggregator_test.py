import unittest
import pandas as pd
import numpy as np
from mock_b_template import MockBTemplate
import sys
sys.path.append("../commands")
from data_aggregator import DataAggregator, parse_all_columns

class DataAggregatorTest(unittest.TestCase):
    '''
    Unit tests for the DataAggregator function.
    '''
    
    def setUp(self):
        self.mock_template = MockBTemplate("mock_b_template")
        self.da = DataAggregator("mock_b_template")
        
    def test_initialization(self):
        result = isinstance(self.da, DataAggregator)
        self.assertTrue(result)
        
    def test_all_string_df(self):
        df = pd.DataFrame([['ba','asd',"ss"],['abb','ayy','op'],
                           ['you','are','good']], columns=['a', 'b', 'c'])
        expected_result = ([('c', 0), ('c', 1), ('c', 2)])
        result = parse_all_columns(df, self.mock_template)
        self.assertTrue(expected_result, result)
    
    def test_all_number_df(self):
        df = pd.DataFrame([[1,9,5],[95,3,51],[158,1,5]],
                          columns=['a', 'b', 'c'])
        expected_result = ([('b', 0), ('b', 1), ('b', 2)])
        result = parse_all_columns(df, self.mock_template)
        self.assertTrue(expected_result, result)
    
    def test_mixed_df(self):
        df = pd.DataFrame([[1,'hi',"litt"],[113,'a','2'],['62',15,'a']],
                          columns=['a', 'b', 'c'])
        expected_result = ([('b', 2), ('c', 0), ('c', 2)])
        result = parse_all_columns(df, self.mock_template)
        self.assertTrue(expected_result, result)
    
    def test_diff_regex(self):
        df = pd.DataFrame([['M1M1M1','SS','A'],['H8M3I1','B1','Bb'],['B9M1I21','C9','c']],
                                  columns=['a', 'b', 'c'])
        self.mock_template._regex = ['^([a-zA-z]?[0-9]){3}$','[a-zA-Z]?[0-9]', '[a-z]']
        expected_result = ([('a', 2), ('b', 0), ('c', 0), ('c', 1)])
        result = parse_all_columns(df, self.mock_template)
        self.assertTrue(expected_result, result)
<<<<<<< HEAD

if __name__ == '__main__':
    unittest.main(exit=False)
=======
    
if __name__ == '__main__':
    unittest.main(exit=False)
>>>>>>> ee325ce85d8a90b6b492cd8d0324bba40f604e15

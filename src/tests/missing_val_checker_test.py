import unittest
import pandas as pd
import numpy as np
from template_client import TemplateClient
from mock_template import MockTemplate
import sys
sys.path.append("../commands")
from missing_val_checker import MissingValChecker

class MissingValCheckerTest(unittest.TestCase):
    '''
    '''
    
    def setUp(self):
        self.template_client = TemplateClient()
        self.mock_template = MockTemplate("mock_template", "a")
        self.template_client.add_template("mock_template", self.mock_template)
        self.mv = MissingValChecker("mock_template")
        
    def test_initialization(self):
        result = isinstance(self.mv, MissingValChecker)
        self.assertTrue(result)
        
    def test_empty_dataframe(self):
        df = pd.DataFrame(columns=[])
        expected_result = [("a", -1), ("e", -1), ("f", -1)]
        result = self.mv.execute(df, self.template_client)
        self.assertCountEqual(expected_result, result)
        
if __name__ == '__main__':
        unittest.main(exit=False)
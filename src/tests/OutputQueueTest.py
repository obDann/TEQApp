import sys
import unittest

import pandas as pd
import numpy as np



'''Import OutputQueue'''
sys.path.insert(0, "../output")
from OutputQueue import *


class TestOutputQueue(unittest.TestCase):
    '''
    A test for the Output Queue class
    '''

    def setUp(self):
        '''
        Set up the queue
        '''
        self.our_q = OutputQueue()

    def test_initialization(self):
        result = isinstance(self.our_q, OutputQueue)
        self.assertTrue(result)

    def test_empty_on_initialization(self):
        result = self.our_q.is_empty()
        self.assertTrue(result)

    def test_enqueue_once(self):
        test_str = "test string"
        self.our_q.enqueue(test_str)
        # we don't expect that this is empty
        result = not self.our_q.is_empty()
        self.assertTrue(result)

    def test_enqueue_once_num_objs(self):
        test_str = "test string"
        self.our_q.enqueue(test_str)
        # we expect that there is only one object
        result = self.our_q.how_many()
        expected = 1
        self.assertEqual(expected, result)

    def test_enqueue_three_objs(self):
        test_str = "test string"
        # make a test dataframe
        some_df = pd.DataFrame(np.random.randint(low=0, high=10, size=(5, 5)),
                           columns=['a', 'b', 'c', 'd', 'e'])
        # make another string
        another_str = "another string"

        # save those three in the queue
        self.our_q.enqueue(test_str)
        self.our_q.enqueue(some_df)
        self.our_q.enqueue(another_str)

        # we expect that there are 3 objects
        result = self.our_q.how_many()
        expected = 3
        self.assertEqual(expected, result)


    def test_enqueue_three_objs_order(self):
        test_str = "test string"
        # make a test dataframe
        some_df = pd.DataFrame(np.random.randint(low=0, high=10, size=(5, 5)),
                           columns=['a', 'b', 'c', 'd', 'e'])
        # make another string
        another_str = "another string"

        # save those three in the queue
        self.our_q.enqueue(test_str)
        self.our_q.enqueue(some_df)
        self.our_q.enqueue(another_str)

        # then dequeue them
        first_result = self.our_q.dequeue()
        second_result = self.our_q.dequeue()
        third_result = self.our_q.dequeue()

        self.assertEqual(test_str, first_result)
        self.assertTrue(some_df.equals(second_result))
        self.assertEqual(another_str, third_result)

if __name__ == '__main__':
    unittest.main(exit=False)

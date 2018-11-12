import unittest
import sys
'''
Import commands
'''
sys.path.insert(0, "../../temhelp")
from dropdown_processor import *


class TestDropdownProcessor(unittest.TestCase):

    def setUp(self):
        # just create a self.dropdown_procesor
        self.ddproc = DropdownProcessor()

    def test_column_is_dropdown(self):
        # we know that "Unique Identifier" is a dropdown value in the template
        my_column = "Unique Identifier"
        behaviour = self.ddproc.is_dropdown(my_column)
        # we expect that this is true
        self.assertTrue(behaviour)

    def test_dropdown_options(self):
        # we know that "Type of Service" is a dropdown value in the template
        my_column = "Type of Service"
        # we make our expected values
        expected = ["Conversation circle",
                    "Targeted matching between newcomer and settled "
                    + "immigrant or long-time Canadian",
                    "Networking activity with other newcomers "
                    + "or Canadian citizens",
                    "Youth leadership project", "Other regular group "
                    + "activities to address ongoing needs or interests",
                    ]
        # and then our actual values
        actual = self.ddproc.get_options(my_column)

        # from here, we just test whether or not this is equal
        self.assertEqual(actual, expected)

    def test_is_column_nondropdown(self):
        # we know that "Date of Birth" is not a dropdown value
        my_column = "Date of Birth"
        # get the behaviour
        behaviour = self.ddproc.is_dropdown(my_column)
        # we expect that this is false
        self.assertFalse(behaviour)

    def test_no_column_options(self):
        # we know that "Postal Code" is not a dropdwn value
        my_column = "Postal Code"
        # we know that this will raise an error
        self.assertRaises(DataNotEnteredException,
                          self.ddproc.get_options, my_column)


if __name__ == '__main__':
    unittest.main(exit=False)
    # testing for all other columns in the csv is rigorous in nature,
    # that is why it is why only two entries from the csv is found to be
    # sensible.

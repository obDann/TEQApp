import unittest
import sys
'''
Import commands
'''
sys.path.insert(0, "../../temhelp")
from template_processor import *


class TestTemplateProcessor(unittest.TestCase):

    def setUp(self):
        # create a template processor
        self.tem_proc = TemplateProcessor()

    def test_template_has_entered_metadata(self):
        # we know that community connections is a template that has metadata
        my_template = "Community Connections"
        behaviour = self.tem_proc.is_entered_metadata(my_template)
        self.assertTrue(behaviour)

    def test_template_no_entered_metadata(self):
        # we know that 'awoogawoo' is not a template that has metadata
        my_template = 'awoogawoo'
        behaviour = self.tem_proc.is_entered_metadata(my_template)
        self.assertFalse(behaviour)

    def test_get_relative_metadata(self):
        # we know that "Language Training - Client Exit" is a template
        my_template = "Language Training - Client Exit"
        # so we get the expected

        # 'ls' stands for long strings
        ls_1 = '[BUID:305939,RID:,ORP:4/5,DTS:2018-08-07 10:05:04][1] '
        ls_1 += '(Client) Unable to validate against database. / '
        ls_1 += '(Client) Impossible de valider dans la base de'
        ls_2 = 'FOSS/GCMS Client ID'
        ls_3 = 'Unique Identifier Value'
        ls_4 = 'Client Date of Birth (YYYY-MM-DD)'
        ls_5 = '([A-Z])-([A-Z]){6}\\d{5}'
        ls_6 = "Client's Training Status"
        ls_7 = 'Date Client Exited Course (YYYY-MM-DD)'
        ls_8 = 'Reason for Exiting course'
        ls_9 = 'Was a Certificate issued to the client?'
        ls_10 = 'Listening level indicated on Certificate'
        ls_11 = 'Speaking level indicated on Certificate'
        expected_dict = {'Processing Details': ('0', '(?s).*', ls_1),
                         'Update record ID': ('0', '[0-9]{8}', '10387104'),
                         'Unique Identifier Type': ('1', '', ls_2),
                         ls_3: ('0', '[0-9]{8,10}', '12345678'),
                         ls_4: ('0', '\\d{4}-\\d{2}-\\d{2}', '1978-05-20'),
                         'Course Code': ('0', ls_5, 'L-CCSMARS18008'),
                         ls_6: ('1', '', 'Completed the course'),
                         ls_7: ('0', '\\d{4}-\\d{2}-\\d{2}', '2018-07-20'),
                         ls_8: ('1', '', 'Found employment'),
                         'Listening CLB Level': ('1', '', 'N/A'),
                         'Speaking CLB Level': ('1', '', 'N/A'),
                         'Reading CLB Level': ('1', '', 'N/A'),
                         'Writing CLB Level': ('1', '', 'N/A'),
                         ls_9: ('1', '', 'Yes'),
                         ls_10: ('1', '', 'N/A'),
                         ls_11: ('1', '', 'N/A'),
                         'Support services received': ('1', '', 'Yes'),
                         'Care for newcomer children': ('1', '', 'Yes'),
                         'Child 1: Age': ('1', '', 'Infant (6-18 months)'),
                         'Child 1: Type of Care': ('1', '', 'Short term'),
                         'Child 2: Age': ('1', '', 'Infant (6-18 months)'),
                         'Child 2: Type of Care': ('1', '', 'Short term'),
                         'Child 3: Age': ('1', '', 'Infant (6-18 months)'),
                         'Child 3: Type of Care': ('1', '', 'Short term'),
                         'Child 4: Age': ('1', '', 'Infant (6-18 months)'),
                         'Child 4: Type of Care': ('1', '', 'Short term'),
                         'Child 5: Age': ('1', '', 'Infant (6-18 months)'),
                         'Child 5: Type of Care': ('1', '', 'Short term'),
                         'Transportation': ('1', '', 'Yes'),
                         'Provisions for disabilities': ('1', '', 'Yes'),
                         'Translation': ('1', '', 'Yes'),
                         'Translation language Between': ('1', '', 'English'),
                         'Translation language And': ('1', '', 'English'),
                         'Interpretation': ('1', '', 'Yes'),
                         'Between': ('1', '', 'English'),
                         'And': ('1', '', 'English'),
                         'Crisis Counselling': ('1', '', 'Yes'),
                         'Reason for update': ('1', '', 'Amend record')}

        expected_mand = ('Unique Identifier Type',
                         'Unique Identifier Value',
                         'Client Date of Birth (YYYY-MM-DD)',
                         'Course Code', "Client's Training Status",
                         'Was a Certificate issued to the client?',
                         'Support services received')
        # get the actual values
        ac_meta, ac_mand = self.tem_proc.get_relative_metadata(my_template)

        # compare the two
        self.assertEqual(ac_meta, expected_dict)
        self.assertEqual(ac_mand, expected_mand)

    def test_get_no_relative_metadata(self):
        # we know that "woohooogooo" is not a template, but let's attempt
        # to get its metadata
        my_template = "woohooogooo"

        # we know that if we get the metadata of this, it will cause
        # an exception
        self.assertRaises(DataNotEnteredException,
                          self.tem_proc.get_relative_metadata, my_template)

if __name__ == '__main__':
    unittest.main(exit=False)
    # testing for all templates is rigorous in nature, that is why
    # only one template is tested

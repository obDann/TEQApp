import unittest
import sys
'''
Import commands
'''
sys.path.insert(0, "../../temhelp")
from true_tem_handler import *


class TestTrueTemplateHandler(unittest.TestCase):

    def setUp(self):
        # we are just going to be dealing with "community connections"
        self.my_th = TrueTemplateHandler("Community Connections")

    def test_no_template_on_init(self):
        # we know that "ahchoo" is not a template name
        template_name = "ahchoo"

        self.assertRaises(TemplateNotEnteredException,
                          TrueTemplateHandler, template_name)

    def test_handle_valid_template(self):
        # we know that in Community Connections, there is a column called
        # "Postal Code where the service was received"
        col = "Postal Code where the service was received"
        # we know that it is in there, it has a regex, and has an example
        expected_regex = "([A-Z]\d){3}"
        expected_example = "M6G3A4"
        in_th, actual_regex, actual_example = self.my_th.handle_template(col)

        # check that it is in there
        self.assertTrue(in_th)
        # check the regex
        self.assertEqual(actual_regex, expected_regex)
        # check the example
        self.assertEqual(actual_example, expected_example)

    def test_handle_template_invalid(self):
        # we know that in Community Connections, "Postal Code" is not
        # a valid column
        col = "Postal Code"

        # so we expect an error
        self.assertRaises(ColumnNotInTemplateException,
                          self.my_th.handle_template, col)

    def test_get_headers(self):
        # just create our headers
        expected = ['Processing Details', 'Update Record ID',
                    'Unique Identifier', 'Unique Identifier Value',
                    'Date of Birth (YYYY-MM-DD)',
                    'Postal Code where the service was received',
                    'Language of Service', 'Official Language of Preference',
                    'Referred By',
                    'Activity Under Which Client Received Services',
                    'Type of Institution/Organization '
                    + 'Where Client Received Services',
                    'Type of Event Attended', 'Type of Service',
                    'Main Topic/Focus of the Service Received',
                    'Service Received', 'Number of Unique Participants',
                    'Did Volunteers from the Host Community '
                    + 'Participate in the Activity',
                    'Directed at a Specific Target Group',
                    'Target Group: Children (0-14 yrs)',
                    'Target Group: Youth (15-24 yrs)', 'Target Group: Senior',
                    'Target Group: Gender-specific', 'Target Group: Refugees',
                    'Target Group: Ethnic/cultural/linguistic group',
                    'Target Group: Deaf or Hard of Hearing',
                    'Target Group: Blind or Partially Sighted',
                    'Target Group: Lesbian, Gay, Bisexual, '
                    + 'Transgender, Queer (LGBTQ)',
                    'Target Group: Families/Parents',
                    'Target Group: Other impairments (physical, mental)',
                    'Target Group: Clients with international '
                    + 'training in a regulated profession',
                    'Target Group: Clients with international '
                    + 'training in a regulated trade',
                    'Target Group: Official language minorities',
                    'Status of Service', 'Reason for Leaving Service',
                    'Start Date (YYYY-MM-DD)', 'End Date (YYYY-MM-DD)',
                    'Projected End Date (YYYY-MM-DD)',
                    'Was Essential Skills and Aptitudes '
                    + 'Training Received as Part of the Service?',
                    'Computer Skills', 'Document Use',
                    'Interpersonal Skills and Workplace Culture',
                    'Leadership Training', 'Life Skills', 'Numeracy',
                    'Support Services Received', 'Care for Newcomer Children',
                    'Child 1: Age', 'Child 1: Type of Care', 'Child 2: Age',
                    'Child 2: Type of Care', 'Child 3: Age',
                    'Child 3: Type of Care', 'Child 4: Age',
                    'Child 4: Type of Care', 'Child 5: Age',
                    'Child 5: Type of Care', 'Transportation',
                    'Provisions for Disabilities', 'Translation', 'Between',
                    'And', 'Interpretation', 'Crisis Counselling',
                    'Total Length of Service: Hours',
                    'Total Length of Service: Minutes', 'Reason for update']
        actual = self.my_th.get_headers()
        # then compare the two
        self.assertEqual(actual, expected)

    def test_get_mandatory_headers(self):
        expected = ['Unique Identifier', 'Unique Identifier Value',
                    'Date of Birth (YYYY-MM-DD)',
                    'Postal Code where the service was received',
                    'Language of Service', 'Official Language of Preference',
                    'Referred By',
                    'Activity Under Which Client Received Services',
                    'Type of Institution/Organization '
                    + 'Where Client Received Services',
                    'Main Topic/Focus of the Service Received',
                    'Service Received', 'Status of Service',
                    'Start Date (YYYY-MM-DD)',
                    'Was Essential Skills and Aptitudes '
                    + 'Training Received as Part of the Service?',
                    'Support Services Received']
        actual = self.my_th.get_mandatory_headers()
        # compare the two
        self.assertEqual(actual, expected)

    def test_col_is_dropdown_mandatory(self):
        # we know that "Unique Identifier" is a dropdown mandatory value
        my_col = "Unique Identifier"
        behaviour = self.my_th.is_dropdown_value_mandatory(my_col)
        self.assertTrue(behaviour)

    def test_col_is_not_dropdown_mandatory(self):
        # we know that "Unique Identifier Value" is not a dropdown mandatory
        # value
        my_col = "Unique Identifier Value"
        behaviour = self.my_th.is_dropdown_value_mandatory(my_col)
        self.assertFalse(behaviour)

    def test_col_not_even_in_template_is_dropdown_mandatory(self):
        # we know that "Wishywashy" is not a column in the template in the
        # first place
        my_col = "Wishywashy"
        self.assertRaises(ColumnNotInTemplateException,
                          self.my_th.is_dropdown_value_mandatory, my_col)

    def test_get_dropdown_vals(self):
        # we know that "Type of Event Attended" is a dropdown
        col_name = "Type of Event Attended"

        expected = ["Events/visits pertaining to culture or history",
                    "Field trip connecting newcomer to community "
                    + "resources or local services",
                    "Sports/recreation event", "Neighbourhood day",
                    "Other community event"]

        actual = self.my_th.get_dropdown_values(col_name)

        self.assertEqual(actual, expected)

    def test_get_dropdown_vals_nondropdown(self):
        # we know that "Unique Identifier Value" is not a dropdown value
        # but is a column in the tempalte
        col_name = "Unique Identifier Value"

        # so we expect an empty list
        expected = []

        actual = self.my_th.get_dropdown_values(col_name)

        self.assertEqual(actual, expected)

    def test_get_dropdown_vals_nonexistant_col(self):
        # we know that "this column" does not exist, so ti will produce an
        # error
        col_name = "this column"
        self.assertRaises(ColumnNotInTemplateException,
                          self.my_th.get_dropdown_values, col_name)

if __name__ == '__main__':
    unittest.main(exit=False)
    # testing all templates is rigorous in nature; hence why there is only
    # one template that's tested

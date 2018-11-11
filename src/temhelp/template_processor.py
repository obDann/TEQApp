import os
import pandas as pd
from data_not_entered_exception import DataNotEnteredException


class TemplateProcessor():
    '''
    An intermediary to help with the template helpers and the vast amounts
    of data that is in the templates. Used strictly for metadata.
    '''
    TH = "\\template_headers.csv"
    PATH = os.path.dirname(os.path.realpath(__file__)) + TH

    def __init__(self):
        '''
        (TemplateProcessor, str) -> None

        Intialize the TemplateProcessor
        '''
        # REPRESENTATION INVARIANT
        # self._intermediary is a pandas' dataframe that holds metadata for
        # the templates provided

        # the first row of the csv file should only contain the entry
        # 'Reference'
        # the first column contains every template handler's name along with
        # concatenation of "Regex" or "Mandatory" or "Dropdown" or "Example"

        self._intermediary = pd.read_csv(self.PATH, index_col=0)

    def get_relative_metadata(self, template_name):
        '''
        (TemplateProcessor, str) -> (dictionary, tuple of str)

        Given a TemplateHandler, this method returns a dictionary such that
        each key is a string representing the column name, and each value is
        a tuple of an integer and two strings. The integer represents whether
        if it is a dropdown column or not, the first string is a regex
        according to the column (this is NaN if the column is a dropdown
        column), and the last string is an example i.e.

        {column_header : (is_dropdown, regex, example)}

        The tuple of strings that is returned is the mandatory fields of that
        specified template

        RAISES DataNotEnteredException if there does not exist metadata
        for the TemplateHandler
        '''
        # check if the template name is not there
        if not (self.is_entered_metadata(template_name)):
            # if it isn't raise an exception
            msg = "Please enter metadata for the class '"
            msg += template_name + "'"
            raise DataNotEnteredException(msg)

        # create our dictionary
        our_dict = {}

        # what we want to do is get the row of the template, these are going
        # to be our headers (we want to drop NAs)
        headers = self._intermediary.loc[template_name].dropna(axis=0,
                                                               how="any")
        headers = list(headers)

        # then what we want is the list of whether or not it is drop down or
        # not
        is_dropdown = list(self._intermediary.loc[template_name + "Dropdown"])
        # the regexes
        regexes = self._intermediary.loc[template_name + "Regex"]
        regexes = regexes.fillna("")
        regexes = list(regexes)
        # the examples
        examples = self._intermediary.loc[template_name + "Example"]
        examples = examples.fillna("N/A")
        examples = list(examples)

        # and the mandatory fields
        template_mand = template_name + "Mandatory"
        mandatory_fields = self._intermediary.loc[template_mand]
        mandatory_fields = mandatory_fields.dropna(axis=0, how="any")
        mandatory_fields = tuple(mandatory_fields)

        # we go through the headers
        for index in range(len(headers)):
            # define the values
            header = headers[index]
            is_this_dropdown = is_dropdown[index]
            regex = regexes[index]
            example = examples[index]
            # use our dictionary to store the values
            our_dict[header] = (is_this_dropdown, regex, example)

        # then return the dictionary and the mandatory fields
        return our_dict, mandatory_fields

    def is_entered_metadata(self, template_name):
        '''
        (TemplateProcessor, str) -> bool

        Determines if there is metadata entered for the template
        '''
        return template_name in self._intermediary.index

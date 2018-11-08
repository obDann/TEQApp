from template_handler import TemplateHandler
from template_processor import *
from template_not_entered_exception import *
from col_not_in_template_exception import *
from data_not_entered_exception import *
from dropdown_processor import *


class TrueTemplateHandler(TemplateHandler):
    '''
    A template Handler that provides the necessary metadata for all possible
    templates
    '''

    def __init__(self, template_name):
        '''
        (TrueTemplateHandler, str, str) -> None

        Initializes a template handler and injects a template name
        and a column name

        RAISES TemplateNotEnteredException if there is no metadata for the
        template
        '''
        # REPRESENTATION INVARIANT
        # self._headers is a list of strings that are the headers of the
        # template
        #
        # self._mand is a list of strings that are the mandatory
        # headers for the template
        #
        # self._md is a dictionary containing metadata of the
        # columns (this includes is_dropdown, regex, and example)
        #
        # self._ddproc is a dropdown processor that is an intermediary for
        # dropdown values

        # first, let's make a template processor and inject the template name
        my_tp = TemplateProcessor()

        # then we want to determine if the data is entered
        try:
            self._md, self._mand = my_tp.get_relative_metadata(template_name)
            # and we can instantiate the headers
            self._headers = list(self._md)
            # convert the tuple into a list for mandatory headers
            self._mand = list(self._mand)
            # and let's create a dropdown processor
            self._ddproc = DropdownProcessor()

        except DataNotEnteredException:
            msg = "there is no metadata for the template " + template_name
            raise TemplateNotEnteredException(msg)

    def handle_template(self, col_name):
        '''
        (TemplateHandler, str) -> tuple of (bool, str, str)

        Returns tuple of a boolean to determine if the injected column name is
        in the template, a string representing the appropriate regex, and a
        string representing an example of the column

        RAISES ColumnNotInTemplateException if the specified column name is
        not in the template
        '''
        # check if the column name is valid
        self._column_name_check(col_name)

        # then we can assume that the column name is within our dictionary
        # so we get the values as follows
        dummy, regex, example = self._md[col_name]
        return True, regex, example

    def get_headers(self):
        '''
        (TemplateHander) -> [List of str]

        Returns a list of headers of this template
        '''
        # just return our headers
        return self._headers

    def get_mandatory_headers(self):
        '''
        (TemplateHandler) -> [List of str]

        Returns a list of mandatory headers in this template
        '''
        # just return mandatory headers
        return self._mand

    def is_dropdown_value_mandatory(self, col_name):
        '''
        (TemplateHandler, col_name) -> bool

        Determines if the column name injected into the template handler
        has strict and limited drop down values

        RAISES ColumnNotInTemplateException if the specified column name is
        not in the template
        '''
        # check if the column name is in the template
        self._column_name_check(col_name)

        # if it is, then we can use our metadata dictionary
        to_return, dummy, dummy = self._md[col_name]

        # the to return variable is a string, so we have to convert it into
        # an int, then into a boolean
        to_return = bool(int(to_return))
        return to_return

    def get_dropdown_values(self, col_name):
        '''
        (TemplateHandler) -> [list of str]

        Returns the list of mandatory dropdown values for the injected
        column name. If the column name is in the template but is not
        dropdown mandatory, this method returns an empty list

        RAISES ColumnNotInTemplateException if the specified column name is
        not in the template
        '''
        # check if the column name is in the template
        self._column_name_check(col_name)

        # then check if it is dropdown mandatory
        if not self.is_dropdown_value_mandatory(col_name):
            return []

        # otherwise, we can return a list using our dropdown processor
        return self._ddproc.get_options(col_name)

    def _column_name_check(self, col_name):
        '''
        (TrueTemplateHandler, str) -> None

        Checks if the column name is in the headers

        RAISES ColumnNotInTemplateException if the specified column name is
        not in the template
        '''
        if col_name not in self._headers:
            # make a message
            msg = "The column name '" + col_name + "' is not in the template"
            raise ColumnNotInTemplateException(msg)


if __name__ == "__main__":
    my_th = TrueTemplateHandler("Needs Assessment & Referrals")

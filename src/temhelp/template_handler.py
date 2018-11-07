from abc import ABC, abstractmethod

class TemplateHandler(ABC):

    def __init__(self, template_name, column_name):
        '''
        (TemplateHandler, str, str) -> None

        Initializes a template handler and injects a template name
        and a column name

        RAISES TemplateNotEnteredException if there is no metadata for the
        column

        RAISES ColumnNotInTemplateException if the specified column name is
        not in the column
        '''
        self._template_name = template_name
        self._column_name = column_name

    @abstractmethod
    def handle_template(self):
        '''
        (TemplateHandler) -> tuple of (bool, str, str)

        Returns tuple of a boolean to determine if the injected column name is
        in the template, a string representing the appropriate regex, and a
        string representing an example of the column
        '''

    @abstractmethod
    def get_headers(self):
        '''
        (TemplateHander) -> [List of str]

        Returns a list of headers of this template
        '''

    @abstractmethod
    def get_mandatory_headers(self):
        '''
        (TemplateHandler) -> [List of str]

        Returns a list of mandatory headers in this template
        '''

    @abstractmethod
    def is_dropdown_value_mandatory(self):
        '''
        (TemplateHandler) -> bool

        Determines if the column name injected into the template handler
        has strict and limited drop down values
        '''

    @abstractmethod
    def get_dropdown_values(self):
        '''
        (TemplateHandler) -> [list of str]

        Returns the list of mandatory dropdown values for the injected
        column name.

        If the column name is not 'dropdown value mandatory', this method
        returns an empty list.
        '''

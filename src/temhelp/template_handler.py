from abc import ABC, abstractmethod

class TemplateHandler(ABC):

    @abstractmethod
    def __init__(self, template_name):
        '''
        (TemplateHandler, str) -> None

        Initializes a template handler and injects a template name

        RAISES TemplateNotEnteredException if there is no metadata for the
        template
        '''

    @abstractmethod
    def handle_template(self, col_name):
        '''
        (TemplateHandler, str) -> tuple of (bool, str, str)

        Returns tuple of a boolean to determine if the injected column name is
        in the template, a string representing the appropriate regex, and a
        string representing an example of the column

        RAISES ColumnNotInTemplateException if the specified column name is
        not in the template
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
    def is_dropdown_value_mandatory(self, col_name):
        '''
        (TemplateHandler, str) -> bool

        Determines if the column name injected into the template handler
        has strict and limited drop down values

        RAISES ColumnNotInTemplateException if the specified column name is
        not in the template
        '''

    @abstractmethod
    def get_dropdown_values(self, col_name):
        '''
        (TemplateHandler, str) -> [list of str]

        Returns the list of mandatory dropdown values for the injected
        column name.

        RAISES ColumnNotInTemplateException if the specified column name is
        not in the template
        '''

from abc import ABC, abstractmethod

class TemplateHandler(ABC):

    def __init__(self, column_name):
        '''
        (TemplateHandler, str) -> None

        Initializes a template handler and injects a column name
        '''
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

class MockBTemplate():
    
    def  __init__(self, template_name):
        '''
        (TemplateHandler, str) -> None

        Initializes a MockTemplate and injects a template name
        and a column name
        '''
        #TemplateHandler.__init__(self, template_name, column_name)
        self._headers = ['a', 'b', 'c']
        self._mandatory_headers = ['a', 'e', 'f']
        self._regex = ['','[a-zA-Z]', '[0-9]']
        self._drop_down_values = []
        
    def handle_template(self):
        '''
        (TemplateHandler) -> tuple of (bool, str, str)

        Returns tuple of a boolean to determine if the injected column name is
        in the template, a string representing the appropriate regex, and a
        string representing an example of the column
        '''
        pass
        
    
    def get_headers(self):
        '''
        (TemplateHander) -> [List of str]

        Returns a list of headers of this template
        '''
        return self._headers
    
    def get_regex(self):
            '''
            (TemplateHander) -> [List of str]
    
            Returns a list of regex of this template
            '''
            return self._regex    
        
    def get_mandatory_headers(self):
        '''
        (TemplateHandler) -> [List of str]

        Returns a list of mandatory headers in this template
        '''
        return self._mandatory_headers

    def is_dropdown_value_mandatory(self):
        '''
        (TemplateHandler) -> bool

        Determines if the column name injected into the template handler
        has strict and limited drop down values
        '''
        pass

    def get_dropdown_values(self, col_name):
        '''
        (TemplateHandler) -> [list of str]

        Returns the list of mandatory dropdown values for the injected
        column name.

        If the column name is not 'dropdown value mandatory', this method
        returns an empty list.
        '''
        return self._drop_down_values
from UserConsole import *

class AgencyConsole(UserConsole):
    '''
    An agency specific console that facilitates the activity of an
    agency account
    '''

    def __init__(self):
        '''
        (AgencyConsole) -> None

        Initializes an agency console
        '''
        # REPRESENTATION INVARIANT
        # AgencyConsole is a Console
        #     thus, AgencyConsole is contracted to run
        #
        # AgencyConsole is a UserConsole
        #     AgencyConsole can be ran through a terminal and inherits
        #     protected methods:
        #         _terminal_show_options
        #         _terminal_input_checker
        #         _terminal_run_console
        #     inherits the protected property of
        #         _options (a list of strings)
        #               _options maintains the property that
        #               _options[-1] is the string 'Quit'
        #     and is contracted to implement the abstract method
        #         _run_str_method
        #
        # self._options is the list of options an agency account can do

        # make an options list
        self._options = ["Upload Data", "Quit"]

    def run_console(self):
        '''
        (AgencyConsole) -> None

        Runs the agency console
        '''
        # this will be ran until a possible GUI is made
        self._terminal_run_console()

    def _run_str_method(self, str_method):
        '''
        (AgencyConsole, str) -> OutputQueue [tentative]

        Executes a method within the AgencyConsole where str_method is a
        string from Agency's option list (except for Quit)
        '''
        # what can be done is that we change the string to
        # lowercase
        method_exec = str_method.lower()
        # then we want to replace each space with an underscore
        method_exec = method_exec.replace(" ", "_")
        # and prepend an underscore and the word "terminal"
        method_exec = "_" + method_exec
        # and then execute the method within the class
        result = getattr(self, method_exec)()
        return result

    def _upload_data(self):
        '''
        (TEQConsole, str) -> OutputQueue [this is tentative]

        Uploads the data to the database and returns an OutputQueue in
        regards to the activity
        '''
        print("I am in 'upload data', but I am not implemented yet!")

if __name__ == '__main__':
    a = AgencyConsole()
    a.run_console()

from user_console import *

class TEQConsole(UserConsole):
    '''
    A TEQ specific Console that facilitates the activity of a TEQ account
    '''

    def __init__(self):
        '''
        (TEQConsole) -> None

        Initializes a TEQ Console
        '''
        # REPRESENTATION INVARIANT
        # TEQConsole is a Console
        #     thus, TEQConsole is contracted to run
        #
        # TEQConsole is a UserConsole
        #     thus, TEQConsole can be ran through a terminal and inherits
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
        # self._options is the list of options a TEQ account can do


        # make an options list
        self._options = ["Make Account", "Make Reports", "Quit"]


    def run_console(self):
        '''
        (TEQConsole) -> None

        Runs the TEQ Console
        '''
        # this will be ran until a possible GUI is made
        self._terminal_run_console()


    def _run_str_method(self, str_method):
        '''
        (TEQConsole, str) -> OutputQueue [tentative]

        Executes a method within the TEQConsole where str_method is a string
        from TEQ's option list (except for Quit)
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

    def _make_account(self):
        '''
        (TEQConsole, str) -> OutputQueue [this is tentative]

        Makes an account and returns an output queue in regards to the
        activity
        '''
        print("I am in 'make account', but I am not implemented yet!")

    def _make_reports(self):
        '''
        (TEQConsole, str) -> OutputQueue [this is tentative]

        Makes a report and returns an output queue in regards to the activity
        '''
        print("I am in 'make reports', but I am not implemented yet!")

if __name__ == '__main__':
    a = TEQConsole()
    a.run_console()

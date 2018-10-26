from abc import ABC, abstractmethod
from Console import *

class UserConsole(Console):

    def __init__(self):
        '''
        (UserConsole) -> None

        Initializes a Console for a user
        '''
        # REPRESENTATION INVARIANT
        # UserConsole is a Console
        # UserConsole is contracted to run
        #
        # self._options is a protected list of options of what a user
        # can do
        # self._options[-1] will always be the string 'Quit'
        #
        # For every option (aside from Quit) in self._options, there
        # should be a method where its string is in lowercase, there is an
        # underscore prepending it, and its spaces are replaced by underscores
        #
        # i.e.
        #     if there is an option of "Make Cheese"
        #         There is a method in TEQConsole called _make_cheese()

        # make an 'options' list
        self._options = ["Quit"]

    @abstractmethod
    def _run_str_method(self, str_method):
        '''
        (UserConsole, str) -> OutputQueue [tentative]

        Executes a method within a UserConsole where str_method is a string
        from an option list (except for Quit).

        This method is abstracted for the benefit of dynamic binding
        '''

    def _terminal_show_options(self):
        '''
        (UserConsole) -> str

        Shows the options for a UserAccount and returns the user's input.

        The user's input is in string
        '''
        # go through the list
        for index in range(len(self._options)):
            print(str(index + 1) + " - " + self._options[index])
        user_input = input("Please select your option:\n")
        return user_input


    def _terminal_input_checker(self, user_input):
        '''
        (UserConsole, str) -> bool

        Returns true iff the user input is valid and corresponds to
        the options presented to the user
        '''
        # let's make an invalid message
        msg = "Invalid option. Please insert an option between 1 to "
        msg += str(len(self._options)) + "."
        result = False

        # check if the input is numeric
        if (not user_input.isnumeric()):
            # if it isn't numeric, print out the message and return the
            # result
            print(msg)
            return result

        # check if the input is within range
        else:
            # in this case, we can assume that the value is numeric, so
            # we can turn it into a string
            user_input = int(user_input)
            # then check if it is in range
            if (user_input in range(1, len(self._options) + 1)):
                # if it is, then it's good
                return True
            else:
                # otherwise
                print(msg)
                return False


    def _terminal_run_console(self):
        '''
        (TEQConsole) -> None

        Runs the TEQConsole on the terminal
        '''
        # initialize the user option
        user_option = ""
        # run an infinite while loop until the user quits
        while (user_option != self._options[-1]):
            # show the options and get the input
            indexed_option = self._terminal_show_options()
            # then check if the input is valid
            if (self._terminal_input_checker(indexed_option)):
                # we can set the indexed option as an int
                indexed_option = int(indexed_option) - 1
                # then we want to set the user option to be the index
                user_option = self._options[indexed_option]
                # check if the user option is not "Quit"
                if (user_option != self._options[-1]):
                    # if it isn't quit, then we want to run a custom method
                    # yay for reflection
                    self._run_str_method(user_option)
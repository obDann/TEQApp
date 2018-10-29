from UserConsole import *
import sys
'''
Import commands
'''
sys.path.insert(0, "../commands")
from FileSystemFetcher import *


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
        self._terminal_upload()

    def _terminal_upload(self):
        '''
        (TEQConsole, str) -> OutputQueue [this is tentative]

        Uploads the data from an excel file to the database, and returns
        an OutputQueue in regards to the activity
        '''
        flag = False

        # make a templates list
        templates = ["Client Profile", "Needs Assessment & Referrals",
                     "Community Connections", "Information and Orientation",
                     "Employment Related Services",
                     "Language Training - Client Enrol",
                     "Language Training - Course Setup",
                     "Language Training - Client Exit",
                     "Quit"]
        # do an infinite while loop until the user selects a valid option
        not_valid = True
        while not_valid:
            # check if the first input is an invalid one
            if (flag):
                print("Please input an appropriate number")
            # then set the flag to true
            flag = True
            # go through the templates' list
            index = 0
            print("What template would you like to upload?")
            for index in range(0, len(templates)):
                print(str(index + 1) + " - " + templates[index])
            # get the user's input
            user_input = input()

            # check if the user's input is numeric
            if (user_input.isnumeric()):
                # if it is, then we have to change it to a number
                user_input = int(user_input)
                # then check if it is in range
                not_valid = not user_input in range(1, len(templates) + 1)
                # if it is valid, we can decrement the index by 1
                if (not not_valid):
                    user_input -= 1

        # check if the template is not 'Quit'
        if (user_input != len(templates) - 1):

            print("Select the file corresponding to '" + templates[user_input]
                  + "'")
            # so we can now call our file system fetcher
            our_fsf = FileSystemFetcher()
            excel_rep = our_fsf.execute()

            msg = "Still waiting for other commands to be implemented\n"
            msg += "In the mean time, here's a representation of your "
            msg += "excel file (of a random sheet):"
            print(msg)
            keys = list(excel_rep)
            print(excel_rep[keys[0]].head())


if __name__ == '__main__':
    a = AgencyConsole()
    a.run_console()

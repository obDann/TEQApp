import sys

'''
Import accounts
'''
sys.path.insert(0, "../accounts")
from accounts import Account
from agency_account import AgencyAccount
from teq_account import TEQAccount

from console import Console
from agency_console import AgencyConsole
from user_console import UserConsole
from teq_console import TEQConsole

class MainConsole(Console):
    '''
    A Console to redirect Account Specific Consoles
    '''

    def __init__(self):
        '''
        (MainConsole, Account) -> None

        Initalizes the main console
        '''
        # REPRESENTATION INVARIANT
        # MainConsole is a Console
        # The console can be ran
        #
        # _account is an account, which will redirect to run
        # the account's specific console
        self._account = None


    def inject_account(self, account):
        '''
        (MainConsole, Account) -> None

        Injects an account into the main console so that the appropriate
        console will be ran (Dependency Injection Design)
        '''
        # just set the account
        self._account = account


    def run_console(self):
        '''
        (MainConsole) -> None

        Runs the account specific console
        '''
        # This is a temporary solution; will use reflection later

        # As for now, we don't have any conventions and this makes life much
        # worse
        if (type(self._account) is AgencyAccount):
            # make an agency console
            our_console = AgencyConsole()
            our_console.run_console()
        elif (type(self._account) is TEQAccount):
            our_console = TEQConsole()
            our_console.run_console()

if __name__ == '__main__':
    # BAD CONVENTIONS!
    my_acc = AgencyAccount('name', 'idnum')
    my_console = MainConsole()
    my_console.inject_account(my_acc)
    my_console.run_console()

    my_acc = TEQAccount('name', 'idnum', 'level')
    my_console.inject_account(my_acc)
    my_console.run_console()

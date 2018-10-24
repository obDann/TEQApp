from accounts import account
from agencyAccount import agencyAccount

class TEQ_Account(account):
    def __init__(self, name, numID, level):
        account.__init__(self,name, numID)
        self.level = level # user level (low, medium, high)
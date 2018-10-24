from accounts import account

class agencyAccount(account):
    def __init__(self, agency_name, idNum):
        account.__init__(self, agency_name, idNum);

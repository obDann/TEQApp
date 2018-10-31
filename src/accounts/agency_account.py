from accounts import Account


class AgencyAccount(Account):
    def __init__(self, agency_name, id_num):
        Account.__init__(self, agency_name, id_num)

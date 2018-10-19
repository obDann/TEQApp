from accounts import account

class agencyAccount(account):
    def __init__(self, agency_name, idNum, user_name, password):
        account.__init__(self, agency_name, idNum, user_name, password);
        
    # Not sure if this is gonna be here or not
    def upload_Data(self, file, database):
        return None
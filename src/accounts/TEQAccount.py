from accounts import account
from agencyAccount import agencyAccount

class TEQ_Account(account):
    def __init__(self, name, numID, user_name, password, level):
        account.__init__(self,name, numID, user_name, password)
        self.level = level # user level (low, medium, high)
    
    def upload_Data(self, file, database):
        return None
    
    def generate_Report(self):
        return None
    
    def add_data_templates(self, new_template):
        return None
    
    def create_TEQ_account(self, name, numID, user_name, password, level):
        if (self.logged_in):
            return TEQ_Account(name, numID, user_name, password, level)
    
    def create_agency_account(self,agency_name, idNum, user_name, password):
        if (self.logged_in):
            return agencyAccount(agency_name, idNum, user_name, password)
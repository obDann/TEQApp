class TEQ_Account:
    def __init__(self, name, numID, user_name, password, level):
        self.name = name
        self.numID = numID
        self.level = level # user level
        # for login
        self.user_name = user_name
        self.password = password        
        self.logged_in = False # login status
    
    def login(self, user_name, password):
        if (self.user_name == user_name and self.password == password):
            self.logged_in = True
    
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

class agencyAccount:
    def __init__(self, agency_name, idNum, user_name, password):
        self.agency_name = agency_name
        self.idNum = idNum
        # For login
        self.user_name = user_name
        self.password = password
        self.logged_in = False
    
    def login(self, user_name, password):
        if (self.user_name == user_name and self.password == password):
            self.logged_in = True
            
    # Not sure if this is gonna be here or not
    def upload_Data(self, file, database):
        return None
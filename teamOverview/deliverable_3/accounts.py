class account:
    def __init__(self, name, numID, user_name, password):
        self.name = name
        self.numID = numID
        # for login
        self.user_name = user_name
        self.password = password        
        self.logged_in = False # login status
    
    def login(self, user_name, password):
        if (self.user_name == user_name and self.password == password):
            self.logged_in = True
    
    def log_out(self):
        self.logged_in = False
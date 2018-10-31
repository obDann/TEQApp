from accounts import Account


class TEQAccount(Account):
    def __init__(self, name, num_id, level):
        Account.__init__(self, name, num_id)
        self.level = level  # user level (low, medium, high)

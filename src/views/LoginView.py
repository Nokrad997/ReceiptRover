class LoginView:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def getEmail(self):
        return self.email
    
    def getPassword(self):
        return self.password
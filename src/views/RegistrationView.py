class RegistrationView:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.confirm_password = ""

    def set_credentials(self, username, password, confirm_password):
        self.username = username
        self.password = password
        self.confirm_password = confirm_password

from src.models.Users import Users
import re

class RegistrationController:
    def __init__(self, registrationView, userModel):
        self.registrationView = registrationView
        self.userModel = userModel

    def registerUser(self):
        if self.validateEmail():
            if self.validatePassword():
                self.userModel = Users(self.registrationView.name, self.registrationView.email, self.registrationView.password)
            
                res = self.userModel.addUser()
            
                if isinstance(res, Exception):
                    return "chyba zly email ale nw"
                
                else:
                    return "zydek dodany"
            else:
                return "blad hasla"
        else:
            return "blad emaila"
            
    def validateEmail(self):
        email = self.registrationView.email
        
        email_regex = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

        if re.match(email_regex, email):
            return True
        else:
            return False
        
        

    def validatePassword(self):
        pwd = self.registrationView.password
        
        if(len(pwd) < 8 or len(pwd) > 32):
            return False

        return True
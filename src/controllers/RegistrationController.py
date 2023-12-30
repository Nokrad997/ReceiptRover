from src.models.Users import Users
import re

class RegistrationController:
    def __init__(self, registrationView, userModel):
        self.registrationView = registrationView
        self.userModel = userModel

    def registerUser(self):
        try:
            if self.validateEmail() and self.validateName() and self.validatePassword():

                self.userModel = Users(0, self.registrationView.name, self.registrationView.email, self.registrationView.password)
                res = self.userModel.addUser()
                    
                if isinstance(res, Exception):
                    return "chyba zly email ale nw"    
                
                else:
                    return "zydek dodany"
        
        except Exception as e:
            return e
            
            
    def validateEmail(self):
        email = self.registrationView.email
        
        email_regex = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

        if re.match(email_regex, email):
            return True
        
        else:
            raise Exception("Invalid email address!")
    
    def validateName(self):
        name = self.registrationView.name
        
        if(len(name) < 3 or len(name) > 32):
            raise Exception("Name must be between 3 and 32 characters long!")

        return True

    def validatePassword(self):
        pwd = self.registrationView.password
        rePwd = self.registrationView.reTypePassword
        
        if(len(pwd) < 8 or len(pwd) > 32):
            raise Exception("Password must be between 8 and 32 characters long!")
        
        elif(pwd != rePwd):
            raise Exception("Passwords do not match!")
        
        return True
from src.modelsOnline.User import User
from src.views.RegistrationView import RegistrationView
from src.repositories.UserRepository import UserRepository
import re

class RegistrationController:
    def __init__(self, registrationView : RegistrationView = None, userRepository : UserRepository = None):
        self.registrationView = registrationView
        self.userRepository = userRepository

    def registerUser(self):
        try:
            if self.validateName() and self.validatePassword():

                usr = User(id = 0, name = self.registrationView.name, email = self.registrationView.email, password = self.registrationView.password)
                res = self.userRepository.createUser(usr)
                    
                if isinstance(res, Exception):
                    return "chyba zly email ale nw"    
                
                else:
                    return "zydek dodany"
        
        except Exception as e:
            return e
            
    
    def validateName(self):
        name = self.registrationView.name
        
        if(len(name) < 3 or len(name) > 32):
            raise ValueError("Name must be between 3 and 32 characters long!")

        return True

    def validatePassword(self):
        pwd = self.registrationView.password
        rePwd = self.registrationView.reTypePassword
        
        if(len(pwd) < 8 or len(pwd) > 32):
            raise ValueError("Password must be between 8 and 32 characters long!")
        
        elif(pwd != rePwd):
            raise ValueError("Passwords do not match!")
        
        return True
from src.repositories import UserRepository
from src.views.LoginView import LoginView
import bcrypt

class LoginController:
    def __init__(self, loginView : LoginView, userRepository : UserRepository):
        self.loginView = loginView
        self.userRepository = UserRepository
    
    def login(self):
        email = self.loginView.getEmail()
        password = self.loginView.getPassword()
        usr = self.userModel.getUserByEmail(email)
        if(isinstance(usr, UserController)):
            if(self.userModel.checkPassword(password, usr.getPassword())):
                return "zalogowano"
            else:
                return "zle haslo"
            
        
        else:
            return "zly email"    
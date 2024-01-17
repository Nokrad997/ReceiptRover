from src.repositories import UserRepository
from src.views.LoginView import LoginView
import bcrypt

class LoginController:
    def __init__(self, loginView : LoginView, userModel : UserRepository):
        self.loginView = loginView
        self.userModel = userModel
    
    def login(self):
        email = self.loginView.getEmail()
        password = self.loginView.getPassword()
        usr = self.userModel.getUserByEmail(email)
        if(isinstance(usr, UserRepository)):
            if(self.userModel):
                return "zalogowano"
            else:
                return "zle haslo"
        
        else:
            return "zly email"    
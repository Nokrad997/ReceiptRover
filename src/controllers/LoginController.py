from src.repositories.UserRepository import UserRepository
from src.modelsOnline.User import User
from src.views.LoginView import LoginView
import bcrypt

class LoginController:
    def __init__(self, loginView : LoginView, userRepository : UserRepository):
        self.loginView = loginView
        self.userRepository = userRepository
    
    def login(self):
        email = self.loginView.getEmail()
        password = self.loginView.getPassword()
        usr = self.userRepository.getUserByEmail(email)

        if(isinstance(usr, User)):
            if(self.checkPassword(password, usr.getPassword())):
                return "zalogowano"
            else:
                return "zle haslo"
            
        else:
            return "zly email"    
        
    def checkPassword(self, password, hashedpassword):
        return bcrypt.checkpw(password.encode('utf-8'), hashedpassword.encode('utf-8'))
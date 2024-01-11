from src.models.User import Users
import bcrypt

class LoginController:
    def __init__(self, loginView, userModel):
        self.loginView = loginView
        self.userModel = userModel
    
    def login(self):
        email = self.loginView.email
        password = self.loginView.password
        usr = self.userModel.getUserByEmail(email)
        if(isinstance(usr, Users)):
            if(bcrypt.checkpw(password.encode('utf-8'), usr.password.encode('utf-8'))):
                return "zalogowano"
            else:
                return "zle haslo"
        
        else:
            return "zly email"    
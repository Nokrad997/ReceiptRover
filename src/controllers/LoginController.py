from src.repositories.UserRepository import UserRepository
from src.modelsOnline.User import User
from src.views.LoginView import LoginView
from src.exceptions.Exceptions import InvalidPasswordException, UserDoesntExistException
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
            if(self.checkPassword(password, usr.password)):
                return True
            else:
                raise InvalidPasswordException("zle haslo")
            
        else:
            raise UserDoesntExistException("nie ma takiego uzytkownika")   
        
    def checkPassword(self, password, hashedpassword):
        return bcrypt.checkpw(password.encode('utf-8'), hashedpassword.encode('utf-8'))
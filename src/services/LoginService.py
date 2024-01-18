import bcrypt
from src.repositories.UserRepository import UserRepository
from src.modelsOnline.User import User
from src.views.LoginView import LoginView
from src.exceptions.Exceptions import InvalidPasswordException, UserDoesntExistException

class LoginService:
    def __init__(self):
        self.userRepository = UserRepository()

    def login(self, loginView : LoginView):
        email = loginView.getEmail()
        password = loginView.getPassword()
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
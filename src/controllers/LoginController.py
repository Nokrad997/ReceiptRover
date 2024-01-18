from src.views.LoginView import LoginView
from src.services.LoginService import LoginService
import bcrypt

class LoginController:
    def __init__(self):
        self.loginService = LoginService()
        
    def loginUser(self, loginView : LoginView):
        result = self.loginService.login(loginView)
        
        return result
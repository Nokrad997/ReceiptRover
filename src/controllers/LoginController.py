from src.views.View import View
from src.services.LoginService import LoginService
import bcrypt


class LoginController:
    def __init__(self):
        self.loginService = LoginService()

    def loginUser(self, loginView: View):
        result = self.loginService.login(loginView)

        return result

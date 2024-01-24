from src.views.View import View
from src.services.LoginService import LoginService
import bcrypt


class LoginController:
    def __init__(self):
        self.loginService = LoginService()

    def loginUser(self, loginView: View):
        """
        Logs in a user using the provided login view.

        Parameters:
        - loginView (View): The login view containing user credentials.

        Returns:
        - result: The result of the login operation.
        """
        result = self.loginService.login(loginView)

        return result

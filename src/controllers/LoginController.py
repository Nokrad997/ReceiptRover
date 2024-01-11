from controllers.UserController import UserController
from models.User import User
from views.LoginView import LoginView
import bcrypt

class LoginController:
    def __init__(self):
        self.user_controller = UserController()
        self.login_view = LoginView()

    def authenticate_user(self, username, password):
        user_data = self.user_controller.get_user_by_username(username)

        if user_data and self.user_controller.verify_password(user_data[0][2], password):
            print("Authentication successful!")
        else:
            print("Authentication failed.")

    def perform_login(self):
        self.login_view.display_login_prompt()
        username = self.login_view.get_username("test_user")
        password = self.login_view.get_password("test_password")
        self.authenticate_user(username, password)

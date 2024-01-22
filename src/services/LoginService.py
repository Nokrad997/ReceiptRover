import bcrypt
from src.repositories.UserRepository import UserRepository
from src.modelsOnline.User import User
from src.views.View import View
from src.exceptions.Exceptions import InvalidPasswordException, UserDoesntExistException


class LoginService:
    def __init__(self):
        self.userRepository = UserRepository()

    def login(self, loginView: View):
        """
        Logs in a user by checking the provided email and password against the stored user credentials.

        Args:
            loginView (View): The login view containing the email and password.

        Returns:
            bool: True if the login is successful, False otherwise.

        Raises:
            InvalidPasswordException: If the provided password is incorrect.
            UserDoesntExistException: If the user does not exist.
        """
        email = loginView.getEmail()
        password = loginView.getPassword()
        usr = self.userRepository.getUserByEmail(email)

        if isinstance(usr, User):
            if self.checkPassword(password, usr.password):
                return True
            else:
                raise InvalidPasswordException("zle haslo")

        else:
            raise UserDoesntExistException("nie ma takiego uzytkownika")

    def checkPassword(self, password, hashedpassword):
        """
        Checks if the provided password matches the hashed password.

        Args:
            password (str): The plain text password.
            hashedpassword (str): The hashed password.

        Returns:
            bool: True if the password matches, False otherwise.
        """
        return bcrypt.checkpw(password.encode("utf-8"), hashedpassword.encode("utf-8"))

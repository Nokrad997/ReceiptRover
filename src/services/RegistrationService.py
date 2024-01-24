from src.repositories.UserRepository import UserRepository
from src.views.View import View
from src.modelsOnline.User import User
from src.exceptions.Exceptions import (
    UserAlreadyExistsException,
    InvalidNameException,
    InvalidPasswordException,
)


class RegistrationService:
    """
    Service class for user registration.
    """

    def __init__(self):
        self.userRepository = UserRepository()

    def register(self, registrationView: View):
        """
        Registers a new user.

        Args:
            registrationView (RegistrationView): The registration view containing user details.

        Returns:
            bool or Exception: True if registration is successful, otherwise an exception is raised.
        """
        try:
            if self.validateName(registrationView) and self.validatePassword(
                registrationView
            ):
                res = self.userRepository.createUser(
                    User(
                        id=0,
                        name=registrationView.name,
                        email=registrationView.email,
                        password=registrationView.password,
                    )
                )

                if isinstance(res, Exception):
                    raise UserAlreadyExistsException("User already exists!")

                else:
                    return True

        except UserAlreadyExistsException as e:
            return e
        except InvalidNameException as e:
            return e
        except InvalidPasswordException as e:
            return e
        except Exception as e:
            return e

    def validateName(self, registrationView: View):
        """
        Validates the user's name.

        Args:
            registrationView (RegistrationView): The registration view containing user details.

        Raises:
            InvalidNameException: If the name is not between 3 and 32 characters long.

        Returns:
            bool: True if the name is valid.
        """
        name = registrationView.name

        if len(name) < 3 or len(name) > 32:
            raise InvalidNameException("Name must be between 3 and 32 characters long!")

        return True

    def validatePassword(self, registrationView: View):
        """
        Validates the user's password.

        Args:
            registrationView (RegistrationView): The registration view containing user details.

        Raises:
            InvalidPasswordException: If the password is not between 8 and 32 characters long,
                or if the password and re-typed password do not match.

        Returns:
            bool: True if the password is valid.
        """
        pwd = registrationView.password
        rePwd = registrationView.reTypePassword

        if len(pwd) < 8 or len(pwd) > 32:
            raise InvalidPasswordException(
                "Password must be between 8 and 32 characters long!"
            )

        elif pwd != rePwd:
            raise InvalidPasswordException("Passwords do not match!")

        return True

from tkinter import filedialog
from src.controllers.AddReceiptController import AddReceiptController
from src.controllers.RegistrationController import RegistrationController
from src.controllers.LoginController import LoginController
from src.controllers.SynchronizationController import SynchronizationController
from src.views.View import View
from src.exceptions.Exceptions import (
    InvalidPasswordException,
    UserDoesntExistException,
    UserAlreadyExistsException,
    InvalidNameException,
)


class AppController:
    """
    Controller class for the application.
    """

    def __init__(self):
        self.loggedIn = False
        self.registrationController = RegistrationController()
        self.loginController = LoginController()
        self.synchronizationController = SynchronizationController()

    def register(self, registrationView: View):
        """
        Registers a new user.

        Args:
            registrationView (View): The registration view.

        Raises:
            UserAlreadyExistsException: If the user already exists.
            InvalidNameException: If the name is invalid.
            InvalidPasswordException: If the password is invalid.
            Exception: If an unexpected error occurs.
        """
        try:
            self.registrationController.registerUser(registrationView)
        except UserAlreadyExistsException as e:
            print(e)
        except InvalidNameException as e:
            print(e)
        except InvalidPasswordException as e:
            print(e)
        except Exception as e:
            print(e)

    def login(self, loginView: View):
        """
        Logs in a user.

        Args:
            loginView (View): The login view.

        Raises:
            UserDoesntExistException: If the user doesn't exist.
            InvalidPasswordException: If the password is invalid.
            Exception: If an unexpected error occurs.
        """
        try:
            self.loggedIn = self.loginController.login(loginView)
        except UserDoesntExistException as e:
            print(e)
        except InvalidPasswordException as e:
            print(e)
        except Exception as e:
            print(e)

    def addReceipt(self):
        """
        Placeholder method for adding a receipt.
        """
        pass

    def synchronize(self, userId: int):
        """
        Synchronizes data for a user.

        Args:
            userId (int): The ID of the user.
        """
        self.synchronizationController.synchronizeData(userId)

    def addReceiptController(self, addReceiptView: View):
        """
        Creates an instance of AddReceiptController and calls its addReceiptController method.

        Args:
            addReceiptView (View): The add receipt view.
        """
        addReceiptController = AddReceiptController(addReceiptView)
        addReceiptController.addReceiptController()

    def addProduct(self, addReceiptView: View):
        """
        Creates an instance of AddReceiptController and calls its addProduct method.

        Args:
            addReceiptView (View): The add receipt view.
        """
        addReceiptController = AddReceiptController(addReceiptView)
        addReceiptController.addProduct()

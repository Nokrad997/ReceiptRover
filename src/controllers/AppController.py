from tkinter import messagebox

from src.Navigator import Navigator

from src.exceptions.Exceptions import (
    InvalidPasswordException,
    UserDoesntExistException,
    UserAlreadyExistsException,
    InvalidNameException,
)

from src.controllers.AddReceiptController import AddReceiptController
from src.controllers.RegistrationController import RegistrationController
from src.controllers.LoginController import LoginController
from src.controllers.SynchronizationController import SynchronizationController
from src.controllers.HistoryController import HistoryController

from src.views.View import View



class AppController:
    """
    Controller class for the application.
    """

    loggedIn = False
    
    def __init__(self):
        self.registrationController = RegistrationController()
        self.loginController = LoginController()
        self.synchronizationController = SynchronizationController()
        self.historyController = HistoryController()

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
            AppController.loggedIn = self.loginController.loginUser(loginView)
        except UserDoesntExistException as e:
            print(e)
            messagebox.showerror("Login", "User doesn't exist")
        except InvalidPasswordException as e:
            print(e)
            messagebox.showerror("Login", "Invalid password")
        except Exception as e:
            print(e)
            messagebox.showerror("Login", f"Unexpected error: {e}")

        Navigator().navigateBack()
        messagebox.showinfo("Login", "Login successful")

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

    @staticmethod
    def addReceiptController(addReceiptView: View):
        """
        Creates an instance of AddReceiptController and calls its addReceiptController method.

        Args:
            addReceiptView (View): The add receipt view.
        """
        addReceiptController = AddReceiptController(addReceiptView)
        addReceiptController.addReceiptController()

    @staticmethod
    def addProduct(addReceiptView: View):
        """
        Creates an instance of AddReceiptController and calls its addProduct method.

        Args:
            addReceiptView (View): The add receipt view.
        """
        addReceiptController = AddReceiptController(addReceiptView)
        addReceiptController.addProduct()

    def getHistory(self):
        """
        Gets the history from the data provider.

        Returns:
            list: A list of receipts.
            list: A list of dates.
        """
        return self.historyController.getHistory()
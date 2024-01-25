from tkinter import messagebox

from src.Navigator import Navigator

from src.exceptions.Exceptions import (
    InvalidPasswordException,
    UserDoesntExistException,
    UserAlreadyExistsException,
    InvalidNameException,
)

from src.controllers.AddReceiptController import AddReceiptController
from src.controllers.DataController import DataController
from src.controllers.DataAnalysisController import DataAnalysisController
from src.controllers.HistoryController import HistoryController
from src.controllers.LoginController import LoginController
from src.controllers.RegistrationController import RegistrationController
from src.controllers.SynchronizationController import SynchronizationController

from src.views.View import View


class AppController:
    """
    Controller class for the application.
    """

    loggedIn = False
    
    def __init__(self):
        # self.registrationController = RegistrationController()
        # self.loginController = LoginController()
        # self.synchronizationController = SynchronizationController()
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
            messagebox.showerror("Registration", e)
        except InvalidNameException as e:
            print(e)
            messagebox.showerror("Registration", e)
        except InvalidPasswordException as e:
            print(e)
            messagebox.showerror("Registration", e)
        except Exception as e:
            print(e)
            messagebox.showerror("Registration", f"Unexpected error: {e}")
        else:
            messagebox.showinfo("Success", "You have successfully registered!")

        Navigator().navigateBack()

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
            messagebox.showerror("Login", e)
        except InvalidPasswordException as e:
            print(e)
            messagebox.showerror("Login", e)
        except Exception as e:
            print(e)
            messagebox.showerror("Login", f"Unexpected error: {e}")
        else:
            messagebox.showinfo("Login", "Login successful")
        
        Navigator().navigateBack()

    @staticmethod
    def logout(mainView : View):
        AppController.loggedIn = False
        mainView.hide()
        mainView.place()

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
    
    @staticmethod
    def prepareChart(month, year):
        """
        Prepares the charts for the history view.

        Args:
            month (int): The month.
            year (int): The year.

        Returns:
            list: A list of labels.
            list: A list of values.
        """
        dataController = DataController()
        receipts = dataController.loadReceipts()

        dataAnalysisController = DataAnalysisController()
        return dataAnalysisController.getShopStatement(receipts, month, year)
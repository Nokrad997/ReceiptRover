from tkinter import filedialog

from src.controllers.AddReceiptController import AddReceiptController
from src.controllers.RegistrationController import RegistrationController
from src.controllers.LoginController import LoginController
from src.controllers.SynchronizationController import SynchronizationController

from src.views.View import View

from src.exceptions.Exceptions import InvalidPasswordException, UserDoesntExistException, UserAlreadyExistsException, InvalidNameException

class AppController:
    loggedin = False
    
    @staticmethod
    def register(registrationView: View):
        try:
            registrationController = RegistrationController()
            registrationController.registerUser(registrationView)
        
        except UserAlreadyExistsException as e:
            print(e)
        except InvalidNameException as e:
            print(e)
        except InvalidPasswordException as e:
            print(e)
        except Exception as e:
            print(e)
    
    @staticmethod
    def login(loginView: View):
        try:
            loginController = LoginController()
            AppController.loggedIn = loginController.loginUser(loginView)
            print(AppController.loggedIn)
        except UserDoesntExistException as e:
            print(e)
        except InvalidPasswordException as e:
            print(e)    
        except Exception as e:
            print(e)
    
    @staticmethod
    def addReceipt(self):
        pass

    @staticmethod
    def synchronize(self):
        pass
 
    @staticmethod
    def openDialog(addReceiptView: View):
        addReceiptController = AddReceiptController()
        addReceiptController.openDialog(addReceiptView)
        
    
    
    # canva(AppController) -> mainmenu -> registerButton1 -> registerView -> registerBurron2 -> AppController -> register(registerView)
                    
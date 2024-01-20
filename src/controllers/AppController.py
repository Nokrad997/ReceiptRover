from tkinter import filedialog

from src.controllers.AddReceiptController import AddReceiptController
from src.controllers.RegistrationController import RegistrationController
from src.controllers.LoginController import LoginController
from src.controllers.SynchronizationController import SynchronizationController

# from src.views.AddReceiptView import AddReceiptView
from src.views.RegistrationView import RegistrationView
from src.views.LoginView import LoginView
from src.views.View import View

from src.exceptions.Exceptions import InvalidPasswordException, UserDoesntExistException, UserAlreadyExistsException, InvalidNameException

class AppController:
    def __init__(self):
        self.loggedIn = False
        self.addReceiptController = AddReceiptController()
        self.registrationController = RegistrationController()
        self.loginController = LoginController()
        self.synchronizationController = SynchronizationController()
    
    @staticmethod
    def register(self, registrationView: RegistrationView):
        try:
            self.registrationController.registerUser()
        
        except UserAlreadyExistsException as e:
            print(e)
        except InvalidNameException as e:
            print(e)
        except InvalidPasswordException as e:
            print(e)
        except Exception as e:
            print(e)
    
    @staticmethod
    def login(self, loginView: LoginView):
        try:
            self.loggedIn = self.loginController.login()
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
    def openDialog(self, addReceiptView: View):
        self.addReceiptController.openDialog(addReceiptView)
        
    
    
    # canva(AppController) -> mainmenu -> registerButton1 -> registerView -> registerBurron2 -> AppController -> register(registerView)
                    
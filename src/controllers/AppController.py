from src.controllers.RegistrationController import RegistrationController
from src.controllers.LoginController import LoginController
from src.controllers.SynchronizationController import SynchronizationController

from src.views.View import View

from src.exceptions.Exceptions import InvalidPasswordException, UserDoesntExistException, UserAlreadyExistsException, InvalidNameException

class AppController:
    def __init__(self):
        self.loggedIn = False
        self.registrationController = RegistrationController()
        self.loginController = LoginController()
        self.synchronizationController = SynchronizationController()
    
    @staticmethod
    def register(self, registrationView: View):
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
    
    @staticmethod
    def login(self, loginView: View):
        try:
            self.loggedIn = self.loginController.login(loginView)
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
    
        
    
    
    # canva(AppController) -> mainmenu -> registerButton1 -> registerView -> registerBurron2 -> AppController -> register(registerView)
                    
from src.controllers.RegistrationController import RegistrationController
from src.controllers.LoginController import LoginController
from src.controllers.SynchronizationController import SynchronizationController

from src.repositories.UserRepository import UserRepository

from src.views.RegistrationView import RegistrationView
from src.views.LoginView import LoginView

class AppController:
    def __init__(self):
        self.registrationController = RegistrationController()
        self.loginController = LoginController()
        self.synchronizationController = SynchronizationController()
    
    def register(self, registrationView: RegistrationView, userRepository: UserRepository = UserRepository()):
        self.registrationController.registerUser()
    
    def login(self, loginView: LoginView, userRepository: UserRepository = UserRepository()):
        self.loginController.login()
        
    
    
    # canva(AppController) -> mainmenu -> registerButton1 -> registerView -> registerBurron2 -> AppController -> register(registerView)
                    
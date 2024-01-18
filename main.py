from src.modelsOnline.User import User
from src.repositories.UserRepository import UserRepository
from src.controllers.RegistrationController import RegistrationController
from src.controllers.LoginController import LoginController
from src.views.RegistrationView import RegistrationView
from src.views.LoginView import LoginView
import bcrypt



'''

        PISZEMY KURWA CAMEL CASEM :)
        jebacZydow, a nie jebac_zydow
        zrobmy to porzadnie, a nie jakies gówno

'''

rv = RegistrationView("test1", "test@log1.pl", "testtest", "testtest")
rc = RegistrationController(rv, UserRepository())

print(rc.registerUser())

userRepository = UserRepository()

lv = LoginView("test@log1.pl", "testtest")
lc = LoginController(lv, userRepository)

print(lc.login())

# print(bcrypt.checkpw('testtest'.encode('utf-8'), "$2b$12$b6derw0r4Sw2wYE0C2GuU.ecVTku5uzGQtvw3YO/ZyIvYNTJTyLQW".encode('utf-8')))
# print(bcrypt.checkpw('testtest'.encode('utf-8'), "$2b$12$xqLrHQyUN5OOeDlCilkvFOe3GVr0/mG6tckQ2IQjiWgCTz8QhV8Bi".encode('utf-8')))
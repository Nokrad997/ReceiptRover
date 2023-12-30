from src.models.Model import Model
from src.models.Users import Users
from src.controllers.RegistrationController import RegistrationController
from src.views.RegistrationView import RegistrationView

print("chuj")

usr = Users()
rv = RegistrationView("marek", "marucha@mare.pl", "12345678")
rc = RegistrationController(rv, usr)

print(rc.registerUser())
from src.views.View import View
from src.services.RegistrationService import RegistrationService

class RegistrationController:
    def __init__(self):
        self.registrationService = RegistrationService()

    def registerUser(self, registrationView : View):
        result = self.registrationService.register(registrationView)

        return result
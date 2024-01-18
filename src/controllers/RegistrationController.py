from src.views.RegistrationView import RegistrationView
from src.services.RegistrationService import RegistrationService

class RegistrationController:
    def __init__(self):
        self.registrationService = RegistrationService()

    def registerUser(self, registrationView : RegistrationView):
        result = self.registrationService.register(registrationView)

        return result
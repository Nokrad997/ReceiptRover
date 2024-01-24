from src.services.RegistrationService import RegistrationService
from src.views.View import View


class RegistrationController:
    def __init__(self):
        self.registrationService = RegistrationService()

    def registerUser(self, registrationView: View):
        """
        Register a user using the provided registration view.

        Args:
            registrationView (View): The registration view containing user information.

        Returns:
            bool: True if the user is successfully registered, False otherwise.
        """
        result = self.registrationService.register(registrationView)

        return result

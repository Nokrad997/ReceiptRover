class RegistrationView:
    """
    Represents a view for user registration.

    Args:
        name (str): The name of the user.
        email (str): The email address of the user.
        password (str): The password of the user.
        retypePassword (str): The re-typed password for confirmation.

    Attributes:
        name (str): The name of the user.
        email (str): The email address of the user.
        password (str): The password of the user.
        reTypePassword (str): The re-typed password for confirmation.
    """

    def __init__(self, name, email, password, retypePassword):
        self.name = name
        self.email = email
        self.password = password
        self.reTypePassword = retypePassword

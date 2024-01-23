class InvalidPasswordException(Exception):
    """
    Exception raised when an invalid password is provided.

    Args:
        message (str): The error message associated with the exception.
    """

    def __init__(self, message):
        super().__init__(message)


class UserDoesntExistException(Exception):
    def __init__(self, message):
        super().__init__(message)


class UserAlreadyExistsException(Exception):
    """
    Exception raised when a user already exists.

    Args:
        message (str): The error message associated with the exception.
    """

    def __init__(self, message):
        super().__init__(message)


class InvalidNameException(Exception):
    """
    Exception raised when an invalid name is encountered.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        super().__init__(message)


class InvalidEmailException(Exception):
    """
    Exception raised for invalid email addresses.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        super().__init__(message)


class InvalidApiException(Exception):
    """
    Exception raised when an invalid API is encountered.

    Args:
        message (str): The error message associated with the exception.
    """

    def __init__(self, message):
        super().__init__(message)

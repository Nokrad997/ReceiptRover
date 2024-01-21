
class InvalidPasswordException(Exception):
    def __init__(self, message):
        super().__init__(message)

class UserDoesntExistException(Exception):
    def __init__(self, message):
        super().__init__(message)

class UserAlreadyExistsException(Exception):
    def __init__(self, message):
        super().__init__(message)
        
class InvalidNameException(Exception):
    def __init__(self, message):
        super().__init__(message)

class InvalidEmailException(Exception):
    def __init__(self, message):
        super().__init__(message)
        
class InvalidApiException(Exception):
    def __init__(self, message):
        super().__init__(message)
    

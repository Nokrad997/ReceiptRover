
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

# błedy pobierania danych z pliku ----------------------------------------------------------------  
class ErrorSavingXmlException(Exception):
    def __init__(self, message):
        super().__init__(message)
        
class ErrorReadingXmlException(Exception):
    def __init__(self, message):
        super().__init__(message)
        
class ErrorValueParsingException(Exception):
    def __init__(self, message):
        super().__init__(message)
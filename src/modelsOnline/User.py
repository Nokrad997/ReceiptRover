from pydantic import BaseModel, EmailStr


class User(BaseModel):
    """
    Represents a user in the system.
    """

    id: int
    name: str
    email: EmailStr
    password: str

    @property
    def getId(self) -> int:
        """
        Get the user's ID.

        Returns:
            int: The user's ID.
        """
        return self.id

    @property
    def getName(self) -> str:
        """
        Get the user's name.

        Returns:
            str: The user's name.
        """
        return self.name

    @property
    def getEmail(self) -> EmailStr:
        """
        Get the user's email.

        Returns:
            EmailStr: The user's email.
        """
        return self.email

    @property
    def getPassword(self) -> str:
        """
        Get the user's password.

        Returns:
            str: The user's password.
        """
        return self.password

    @getId.setter
    def setId(self, value):
        """
        Set the user's ID.

        Args:
            value (int): The new ID value.
        """
        self.id = value

    @getName.setter
    def setName(self, value):
        """
        Set the user's name.

        Args:
            value (str): The new name value.
        """
        self.name = value

    @getEmail.setter
    def setEmail(self, value):
        """
        Set the user's email.

        Args:
            value (EmailStr): The new email value.
        """
        self.email = value

    @getPassword.setter
    def setPassword(self, value):
        """
        Set the user's password.

        Args:
            value (str): The new password value.
        """
        self.password = value

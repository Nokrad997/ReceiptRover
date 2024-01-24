import bcrypt

from src.exceptions.Exceptions import (
    UserDoesntExistException,
)

from src.modelsOnline.User import User

from src.repositories.Repository import Repository


class UserRepository(Repository):
    def __init__(self):
        super().__init__()

    def createUser(self, user: User):
        """
        Creates a new user in the database.

        Args:
            user (User): The user object containing the user's information.

        Returns:
            list: The result of the database query.
        """
        password = self.hashPassword(user.password).decode("utf-8")
        query = f"INSERT INTO \"User\" (name, email, password) VALUES ('{user.name}', '{user.email}', '{password}') RETURNING *"
        return self.executeQuery(query)

    def getUserById(self, userid):
        """
        Retrieves a user from the database by their ID.

        Args:
            userid (int): The ID of the user.

        Returns:
            list: The result of the database query.
        """
        query = f'SELECT * FROM "User" WHERE user_id = {userid}'
        return self.executeQuery(query)

    def getUserByEmail(self, email):
        """
        Retrieves a user from the database by their email.

        Args:
            email (str): The email of the user.

        Returns:
            User: The user object containing the user's information.
        """
        query = f"SELECT * FROM \"User\" WHERE email = '{email}'"
        userArray = self.executeQuery(query)
        try: 
            return self.returnUser(
                int(userArray[0][0]),
                str(userArray[0][1]),
                str(userArray[0][2]),
                str(userArray[0][3]),
            )
        except IndexError:
            raise UserDoesntExistException("User doesn't exist")

    def updateUserPassword(self, userid, newpassword):
        """
        Updates the password of a user in the database.

        Args:
            userid (int): The ID of the user.
            newpassword (str): The new password.

        Returns:
            list: The result of the database query.
        """
        newpassword = self.hashPassword(newpassword)
        query = f'UPDATE "User" SET password = \'{newpassword.decode("utf-8")}\' WHERE user_id = {userid} RETURNING *'
        return self.executeQuery(query)

    def hashPassword(self, password):
        """
        Hashes a password using bcrypt.

        Args:
            password (str): The password to be hashed.

        Returns:
            bytes: The hashed password.
        """
        salt = bcrypt.gensalt()
        hashedpassword = bcrypt.hashpw(password.encode("utf-8"), salt)
        return hashedpassword

    def returnUser(self, id, name, email, password):
        """
        Creates a User object from the retrieved user information.

        Args:
            id (int): The ID of the user.
            name (str): The name of the user.
            email (str): The email of the user.
            password (str): The password of the user.

        Returns:
            User: The user object.
        """
        user = User(id=id, name=name, email=email, password=password)
        return user

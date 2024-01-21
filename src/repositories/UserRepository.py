from src.modelsOnline.User import User
from src.repositories.Repository import Repository
import bcrypt


class UserRepository(Repository):
    def __init__(self):
        super().__init__()

    def createUser(self, user: User):
        password = self.hashPassword(user.password).decode("utf-8")
        query = f"INSERT INTO \"User\" (name, email, password) VALUES ('{user.name}', '{user.email}', '{password}') RETURNING *"
        return self.executeQuery(query)

    def getUserById(self, userid):
        query = f'SELECT * FROM "User" WHERE user_id = {userid}'
        return self.executeQuery(query)

    def getUserByEmail(self, email):
        query = f"SELECT * FROM \"User\" WHERE email = '{email}'"
        userArray = self.executeQuery(query)
        return self.returnUser(
            int(userArray[0][0]),
            str(userArray[0][1]),
            str(userArray[0][2]),
            str(userArray[0][3]),
        )

    def updateUserPassword(self, userid, newpassword):
        newpassword = self.hashPassword(newpassword)
        query = f"UPDATE \"User\" SET password = '{newpassword}' WHERE user_id = {userid} RETURNING *"
        return self.executeQuery(query)

    def hashPassword(self, password):
        salt = bcrypt.gensalt()
        hashedpassword = bcrypt.hashpw(password.encode("utf-8"), salt)
        return hashedpassword

    def returnUser(self, id, name, email, password):
        user = User(id=id, name=name, email=email, password=password)
        return user

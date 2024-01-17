from src.modelsOnline.User import User
from src.repositories.Repository import Repository
import bcrypt

class UserRepository(Repository):
    def createUser(self, username, password):
        password = self.hashPassword(password)
        query = f"INSERT INTO user (username, password) VALUES ({username}, {password});"
        return self.executeQuery(query)

    def getUserById(self, userid):
        query = f"SELECT * FROM user WHERE userid = {userid};"
        return self.executeQuery(query)
    
    def getUserByEmail(self, email):
        query = f"SELECT * FROM user WHERE email = {email};"
        userArray = self.executeQuery(query)
        return self.createUser(userArray[0], userArray[1], userArray[2], userArray[3])

    def updateUserPassword(self, userid, newpassword):
        newpassword = self.hashPassword(newpassword)
        query = f"UPDATE user SET password = {newpassword} WHERE user_id = {userid};"
        return self.executeQuery(query)

    def hashPassword(self, password):
        salt = bcrypt.gensalt()
        hashedpassword = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashedpassword
    
    def createUser(id, name, email, password):
        user = User(id = id, name = name, email = email, password = password)
        return user
from controllers.DatabaseController import DatabaseController
import bcrypt

class UserController(DatabaseController):
    def createUser(self, username, password):
        password = self.hashPassword(password)
        query = f"INSERT INTO users (username, password) VALUES ({username}, {password});"
        return self.executeQuery(query)

    def getUserByUsername(self, userid):
        query = f"SELECT * FROM users WHERE user_id = {userid};"
        return self.executeQuery(query)

    def getUserById(self, userid):
        query = f"SELECT * FROM users WHERE userid = {userid};"
        return self.executeQuery(query)
    
    def getUserByEmail(self, email):
        query = f"SELECT * FROM users WHERE email = {email};"
        return self.executeQuery(query)

    def updateUserPassword(self, userid, newpassword):
        newpassword = self.hashPassword(newpassword)
        query = f"UPDATE users SET password = {newpassword} WHERE user_id = {userid};"
        return self.executeQuery(query)

    def verifyPassword(self, hashedpassword, inputpassword):
        password = query = f"SELECT password FROM users WHERE user_id = {user_id};"
        return bcrypt.checkpw(inputpassword.encode('utf-8'), hashedpassword)

    def hashPassword(self, password):
        salt = bcrypt.gensalt()
        hashedpassword = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashedpassword
import bcrypt
from src.models.Model import Model

class Users(Model):
    def __init__(self, name = '', email = '', password = ''):
        super().__init__()

        self.name = name
        self.email = email
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode("utf-8")

    def addUser(self):
        return self.executeQuery(f'INSERT INTO "Users" (name, email, password) VALUES (\'{self.name}\', \'{self.email}\', \'{self.password}\') RETURNING *')
    
    def getUsers(self):
        return self.executeQuery('SELECT * FROM "Users"')

import bcrypt
from src.models.Model import Model

class Users(Model):
    def __init__(self, id = 0, name = '', email = '', password = ''):
        super().__init__()

        self.id = id
        self.name = name
        self.email = email
        self.password = password

    def addUser(self):
        hashedpw = bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        return self.executeQuery(f'INSERT INTO "Users" (name, email, password) VALUES (\'{self.name}\', \'{self.email}\', \'{hashedpw}\') RETURNING *')
    
    def getUsers(self):
        return self.executeQuery('SELECT * FROM "Users"')
    
    def getUserByEmail(self, email):
        res = self.executeQuery(f'SELECT * FROM "Users" WHERE email = \'{email}\'')
        
        if(res):
            return Users(res[0][0], res[0][1], res[0][2], res[0][3])
        else:
            return res

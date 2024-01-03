import bcrypt
from src.models.Model import Model
from pydantic import BaseModel, EmailStr
from typing import Self

class Users(Model, BaseModel):
    id : int
    name : str
    email : EmailStr
    password : str
    def __init__(self, id : int = 0, name : str = '', email :str = '', password :str = ''):
        super().__init__()

        self.id = id
        self.name = name
        self.email = email
        self.password = password

    def addUser(self) -> list:
        hashedpw = bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        return self.executeQuery(f'INSERT INTO "Users" (name, email, password) VALUES (\'{self.name}\', \'{self.email}\', \'{hashedpw}\') RETURNING *')
    
    def getUsers(self) -> list[Self]:
        res = self.executeQuery('SELECT * FROM "Users"')
        if (res):
            for i in range(len(res)):
                res[i] = Users(res[i][0], res[i][1], res[i][2], res[i][3])
            return res
        else:
            return res
    
    def getUserByEmail(self, email) -> Self:
        res = self.executeQuery(f'SELECT * FROM "Users" WHERE email = \'{email}\'')
        
        if(res):
            return Users(res[0][0], res[0][1], res[0][2], res[0][3])
        else:
            return res
        
    def getUserById(self, id) -> Self:
        res = self.executeQuery(f'SELECT * FROM "Users" WHERE id = \'{id}\'')
        
        if(res):
            return Users(res[0][0], res[0][1], res[0][2], res[0][3])
        else:
            return res

from pydantic import BaseModel, EmailStr

class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    password: str

    @property
    def getId(self) -> int:
        return self.id
    
    @property
    def getName(self) -> str:
        return self.name
    
    @property
    def getEmail(self) -> EmailStr:
        return self.email
    
    @property
    def getPassword(self) -> str:
        return self.password
    
    @getId.setter
    def setId(self, value):
        self.id = value

    @getName.setter
    def setName(self, value):
        self.name = value

    @getEmail.setter
    def setEmail(self, value):
        self.email = value

    @getPassword.setter
    def setPassword(self, value):
        self.password = value



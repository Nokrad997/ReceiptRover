from pydantic import BaseModel, EmailStr

class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    password: str
    def __init__(self, id = 0, name = '', email = '', password = ''):
        super().__init__()

        self.id = id
        self.name = name
        self.email = email
        self.password = password

    @property
    def get_id(self) -> int:
        return self.id
    
    @property
    def get_name(self) -> str:
        return self.name
    
    @property
    def get_email(self) -> EmailStr:
        return self.email
    
    @property
    def get_password(self) -> str:
        return self.password
    
    @get_id.setter
    def set_id(self, value):
        self.id = value

    @get_name.setter
    def set_name(self, value):
        self.name = value

    @get_email.setter
    def set_email(self, value):
        self.email = value

    @get_password.setter
    def set_password(self, value):
        self.password = value



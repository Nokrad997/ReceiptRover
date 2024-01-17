from pydantic import BaseModel
from typing import Self

class Product(BaseModel):
    name: str
    price: float
    quantity: float
    
    @property
    def getName(self) -> str:
        return self.name
    
    @property
    def getPrice(self) -> float:
        return self.price
    
    @property
    def getQuantity(self) -> float:
        return self.quantity
    
    @getName.setter
    def setName(self, value : str):
        self.name = value

    @getPrice.setter
    def setPrice(self, value : float):
        self.price = value

    @getQuantity.setter
    def setQuantity(self, value : float):
        self.quantity = value

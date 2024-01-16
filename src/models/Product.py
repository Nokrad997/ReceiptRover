from pydantic import BaseModel
from typing import Self

class Product(BaseModel):
    name: str
    price: float
    quantity: float
    
    @property
    def get_name(self) -> str:
        return self.name
    
    @property
    def get_price(self) -> float:
        return self.price
    
    @property
    def get_quantity(self) -> float:
        return self.quantity
    
    @get_name.setter
    def set_name(self, value : str):
        self.name = value

    @get_price.setter
    def set_price(self, value : float):
        self.price = value

    @get_quantity.setter
    def set_quantity(self, value : float):
        self.quantity = value

from src.models.Model import Model
from pydantic import BaseModel
from typing import Self

class Product(Model,BaseModel):
    name: str
    price: float
    quantity: int
    
    def __init__(self,name:str="",price:float=0,quantity:int=0):
        self.name = name
        self.price = price
        self.quantity = quantity
    

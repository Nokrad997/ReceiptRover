from src.controllers.DatabaseController import Model
from src.models.Product import Product
from pydantic import BaseModel
from typing import Self

class Receipt(Model, BaseModel):
    receipt_id: int
    key: str
    receipt: bytes
    
    def __init__(self, receipt_id : int = 0, key : str = '', receipt : bytes = b''):
        super().__init__()
        self.receipt_id = receipt_id
        self.key = key
        self.receipt = receipt
        self.products=[]
    
    @property
    def get_receipt_id(self) -> int:
        return self.receipt_id
    
    @property
    def get_key(self) -> str:
        return self.key
    
    
    @property
    def get_products(self) -> list[Product]:
        return self.products
    
    @get_receipt_id.setter
    def set_receipt_id(self, value : int):
        self.receipt_id = value
    
    @get_key.setter
    def set_key(self, value : str):
        self.key = value


    @get_products.setter
    def set_products(self, value : list[Product]):
        self.products = value

    
        
        
    

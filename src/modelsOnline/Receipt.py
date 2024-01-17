from src.modelsOnline.Product import Product
from pydantic import BaseModel
from typing import Self

class Receipt(BaseModel):
    receiptId: int
    key: str
    receipt: bytes
    
    @property
    def getReceiptId(self) -> int:
        return self.receiptId
    
    @property
    def getKey(self) -> str:
        return self.key
    
    
    @property
    def getProducts(self) -> list[Product]:
        return self.products
    
    @getReceiptId.setter
    def setReceiptId(self, value : int):
        self.receiptId = value
    
    @getKey.setter
    def setKey(self, value : str):
        self.key = value


    @getProducts.setter
    def setProducts(self, value : list[Product]):
        self.products = value

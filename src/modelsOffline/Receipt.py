from src.modelsOffline.Product import Product
from pydantic import BaseModel
from typing import Self

class Receipt(BaseModel):
    key: str
    shop: str
    products: list[Product]

    @property
    def getKey(self) -> str:
        return self.key
    
    @property
    def getShop(self) -> str:
        return self.key
    
    @property
    def getProducts(self) -> list[Product]:
        return self.products
    
    @getKey.setter
    def setKey(self, value : str):
        self.key = value

    @getShop.setter
    def setShop(self, value : str):
        self.key = value

    @getProducts.setter
    def setProducts(self, value : list[Product]):
        self.products = value

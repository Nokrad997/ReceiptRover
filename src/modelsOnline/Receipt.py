from src.modelsOnline.Product import Product
from pydantic import BaseModel
from typing import Self


class Receipt(BaseModel):
    """
    Represents a receipt object.

    Attributes:
        receiptId (int): The ID of the receipt.
        key (str): The key associated with the receipt.
        receipt (bytes): The receipt data.

    Properties:
        getReceiptId (int): Getter method for receiptId.
        getKey (str): Getter method for key.
        getProducts (list[Product]): Getter method for products.

    Setters:
        setReceiptId (int): Setter method for receiptId.
        setKey (str): Setter method for key.
        setProducts (list[Product]): Setter method for products.
    """

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
    def setReceiptId(self, value: int):
        self.receiptId = value

    @getKey.setter
    def setKey(self, value: str):
        self.key = value

    @getProducts.setter
    def setProducts(self, value: list[Product]):
        self.products = value

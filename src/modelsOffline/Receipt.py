from src.modelsOffline.Product import Product
from pydantic import BaseModel
from typing import Self


class Receipt(BaseModel):
    """
    Represents a receipt with key, shop, and a list of products.
    """

    key: str
    shop: str
    products: list[Product]

    @property
    def getKey(self) -> str:
        """
        Get the key of the receipt.

        Returns:
            str: The key of the receipt.
        """
        return self.key

    @property
    def getShop(self) -> str:
        """
        Get the shop of the receipt.

        Returns:
            str: The shop of the receipt.
        """
        return self.key

    @property
    def getProducts(self) -> list[Product]:
        """
        Get the products of the receipt.

        Returns:
            list[Product]: The products of the receipt.
        """
        return self.products

    @getKey.setter
    def setKey(self, value: str):
        """
        Set the key of the receipt.

        Args:
            value (str): The key to set.
        """
        self.key = value

    @getShop.setter
    def setShop(self, value: str):
        """
        Set the shop of the receipt.

        Args:
            value (str): The shop to set.
        """
        self.key = value

    @getProducts.setter
    def setProducts(self, value: list[Product]):
        """
        Set the products of the receipt.

        Args:
            value (list[Product]): The products to set.
        """
        self.products = value

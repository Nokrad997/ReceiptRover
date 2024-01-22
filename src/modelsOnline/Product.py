from pydantic import BaseModel
from typing import Self


class Product(BaseModel):
    """
    Represents a product with a name, price, and quantity.
    """

    name: str
    price: float
    quantity: float

    @property
    def getName(self) -> str:
        """
        Get the name of the product.

        Returns:
            str: The name of the product.
        """
        return self.name

    @property
    def getPrice(self) -> float:
        """
        Get the price of the product.

        Returns:
            float: The price of the product.
        """
        return self.price

    @property
    def getQuantity(self) -> float:
        """
        Get the quantity of the product.

        Returns:
            float: The quantity of the product.
        """
        return self.quantity

    @getName.setter
    def setName(self, value: str):
        """
        Set the name of the product.

        Args:
            value (str): The new name of the product.
        """
        self.name = value

    @getPrice.setter
    def setPrice(self, value: float):
        """
        Set the price of the product.

        Args:
            value (float): The new price of the product.
        """
        self.price = value

    @getQuantity.setter
    def setQuantity(self, value: float):
        """
        Set the quantity of the product.

        Args:
            value (float): The new quantity of the product.
        """
        self.quantity = value

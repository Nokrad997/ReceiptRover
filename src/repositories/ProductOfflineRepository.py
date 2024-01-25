from src.repositories.Repository import Repository
from src.modelsOffline.Product import Product


class ProductOfflineRepository:
    @staticmethod
    def createProduct(self, name, price, quantity):
        """
        Create a new product with the given name, price, and quantity.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The quantity of the product.

        Returns:
            Product: The newly created product object.
        """
        return Product(name, price, quantity)

    @staticmethod
    def createListOfProduct(products: list):
        """
        Create a list of products with the given list of products.

        Args:
            products (list): A list of products.

        Returns:
            list: The newly created list of products.
        """
        return [Product(name = product[0], price = product[2], quantity = product[1]) for product in products]
    
    """zmiany"""

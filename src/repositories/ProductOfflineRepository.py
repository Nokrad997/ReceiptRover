from src.repositories.Repository import Repository
from src.modelsOffline.Product import Product


class ProductOfflineRepository(Repository):
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

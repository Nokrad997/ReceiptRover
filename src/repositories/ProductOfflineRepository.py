from src.repositories.Repository import Repository
from src.modelsOffline.Product import Product


class ProductOfflineRepository(Repository):
    def createProduct(self, name: str, price: float, quantity: int):
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
        print(products)
        return [Product(product["name"], product["price"], product["quantity"]) for product in products]
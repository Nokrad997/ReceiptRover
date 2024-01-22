from src.repositories.Repository import Repository
from src.modelsOffline.Receipt import Receipt
from datetime import datetime
import random
import string


class ReceiptOfflineRepository(Repository):
    def createReceipt(self, shop, products):
        """
        Creates a new Receipt object with a generated key.

        Args:
            shop (str): The name of the shop.
            products (list): A list of products.

        Returns:
            Receipt: The newly created Receipt object.
        """
        key = self.generateKey()
        return Receipt(key, shop, products)

    def generateKey(self):
        """
        Generates a unique key for the Receipt.

        Returns:
            str: The generated key.
        """
        now = datetime.now()
        key = now.strftime("%Y%m%d%H%M%S")
        signs = string.ascii_letters + string.digits
        key += "".join(random.choices(signs, k=10))
        return key

from src.repositories.Repository import Repository
from src.modelsOffline.Receipt import Receipt
from datetime import datetime
import random
import string
from datetime import datetime, timedelta


class ReceiptOfflineRepository:
    def __init__(self):
        pass
    
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
        return Receipt(key = key, shop = shop, products = products)

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
    
    def generateRandomDate(self):
            """
            Generates a random date and time between January 1, 2023 and January 23, 2024.

            Returns:
                str: A string representation of the random date and time in the format "%Y%m%d%H%M%S".
            """
            startDatetime = datetime(2023, 1, 1)
            endDatetime = datetime(2024, 1, 23, 23, 59, 59)
            
            randomTimedelta = timedelta(
                days=random.randint(0, (endDatetime - startDatetime).days),
                hours=random.randint(0, 23),
                minutes=random.randint(0, 59),
                seconds=random.randint(0, 59)
            )
            
            randomDatetime = startDatetime + randomTimedelta
            
            return randomDatetime.strftime("%Y%m%d%H%M%S")

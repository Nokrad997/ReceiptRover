from src.repositories.Repository import Repository
from src.modelsOffline.Receipt import Receipt
from datetime import datetime
import random
import string

class ReceiptOfflineRepository(Repository):
    def createReceipt(self, shop, products):
        key = self.generateKey()
        return Receipt(key, shop, products)
    
    def generateKey(self):
        now = datetime.now()
        key = now.strftime("%Y%m%d%H%M%S")
        signs = string.ascii_letters + string.digits
        key += ''.join(random.choices(signs, k=10))
        return key
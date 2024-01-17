from src.repositories.Repository import Repository
from src.modelsOffline.Receipt import Receipt

class ReceiptOfflineRepository(Repository):
    def createReceipt(self, key, shop, products):
        return Receipt(key, shop, products)
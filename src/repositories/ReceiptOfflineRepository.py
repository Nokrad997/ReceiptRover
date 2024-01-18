
from src.modelsOffline.Receipt import Receipt

class ReceiptOfflineRepository():
    def createReceipt(self, key, shop, products):
        return Receipt(key=key, shop=shop, products=products)
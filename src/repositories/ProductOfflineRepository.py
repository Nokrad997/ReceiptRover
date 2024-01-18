
from src.modelsOffline.Product import Product

class ProductOfflineRepository():
    def createProduct(self, name, price, quantity):
        return Product(name=name, price=price, quantity=quantity)
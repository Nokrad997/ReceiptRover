from src.repositories.Repository import Repository
from src.modelsOffline.Product import Product


class ProductOfflineRepository(Repository):
    def createProduct(self, name, price, quantity):
        return Product(name, price, quantity)

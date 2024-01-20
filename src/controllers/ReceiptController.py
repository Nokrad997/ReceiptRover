from src.modelsOffline.Product import Product
from src.modelsOffline.Receipt import Receipt
# from src.ocrapi.ocr import ocr

from src.repositories.ProductOfflineRepository import ProductOfflineRepository
from src.repositories.ReceiptOfflineRepository import ReceiptOfflineRepository

class ReceiptController:

    def __init__(self, productOfflineRepository : ProductOfflineRepository, receiptOfflineRepository : ReceiptOfflineRepository):
        self.productOfflineRepository = productOfflineRepository
        self.receiptOfflineRepository = receiptOfflineRepository
        
# może do wyjebania
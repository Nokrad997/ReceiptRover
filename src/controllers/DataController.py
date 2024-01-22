from src.services.DataProvider import DataProvider

class DataController:
    def __init__(self):
        self.dataProvider = DataProvider()

    def addReceipt(self, receipt, filePath = "src/localData/Receipts.xml"):
        self.dataProvider.addReceiptToXmlFile(receipt, filePath)

    def loadReceipts(self, filePath = "src/localData/Receipts.xml"):
        return self.dataProvider.loadReceiptsFromXmlFile(filePath)
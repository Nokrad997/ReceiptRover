from src.services.DataProvider import DataProvider

class DataController:
    def __init__(self):
        self.dataProvider = DataProvider()

    def addReceipt(self, receipt, filePath = "data.xml"):
        self.dataProvider.addReceiptToXmlFile(receipt, filePath)

    def loadReceipts(self, filePath = "data.xml"):
        return self.dataProvider.loadReceiptsFromXmlFile(filePath)
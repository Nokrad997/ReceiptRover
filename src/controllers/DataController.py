from src.services.DataProvider import DataProvider

class DataController:
    def __init__(self):
        self.dataProvider = DataProvider()

    def addReceipt(self, receipt):
        self.dataProvider.addReceiptToXmlFile(receipt)

    def loadReceipts(self):
        return self.dataProvider.loadReceiptsFromXmlFile()

    def getUsersLocalKeys(self):
        return self.dataProvider.getkeysFromXML()
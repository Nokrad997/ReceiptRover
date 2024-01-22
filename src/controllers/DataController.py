from src.services.DataProvider import DataProvider


class DataController:
    def __init__(self):
        self.dataProvider = DataProvider()

    def addReceipt(self, receipt):
        """
        Adds a receipt to the XML file.

        Args:
            receipt: The receipt to be added.
        """
        self.dataProvider.addReceiptToXmlFile(receipt)

    def loadReceipts(self):
        """
        Loads receipts from the XML file.

        Returns:
            list: A list of loaded receipts.
        """
        return self.dataProvider.loadReceiptsFromXmlFile()

    def getUsersLocalKeys(self):
        """
        Retrieves the local keys of the users from the data provider.

        Returns:
            list: A list of local keys.
        """
        return self.dataProvider.getkeysFromXML()

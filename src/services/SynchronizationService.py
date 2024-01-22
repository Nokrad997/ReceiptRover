from src.repositories.TransactionRepository import TransactionRepository
from src.repositories.ReceiptRepository import ReceiptRepository
from src.services.DataProvider import DataProvider


class SynchronizationService:
    def __init__(self):
        """
        Initializes a new instance of the SynchronizationService class.
        """
        self.notFoundInLocalKeys = []
        self.notFoundInDatabaseKeys = []

    def checkData(self, userId: int) -> bool:
        """
        Checks the data for synchronization.

        Args:
            userId (int): The ID of the user.

        Returns:
            bool: True if the data is synchronized, False otherwise.
        """
        transactionRepository = TransactionRepository()
        dataProvider = DataProvider()

        userKeys = transactionRepository.getUsersTransactionsKeys(userId)
        userlocalKeys = dataProvider.getkeysFromXML()
        self.notFoundInLocalKeys = [key for key in userKeys if key not in userlocalKeys]
        self.notFoundInDatabaseKeys = [
            key for key in userlocalKeys if key not in userKeys
        ]

        if len(self.notFoundInLocalKeys) != 0 or len(self.notFoundInDatabaseKeys) != 0:
            return False

        return True

    def synchronizeLocal(self):
        """
        Synchronizes the local data.

        This method adds receipts to the local XML file for keys that are not found locally.
        """
        if len(self.notFoundInLocalKeys) == 0:
            return

        receiptRepository = ReceiptRepository()
        dataProvider = DataProvider()
        for key in self.notFoundInLocalKeys:
            receipt = receiptRepository.getReceiptByKey(key)
            dataProvider.addReceiptToXmlFile(receipt)

    def synchronize_database(self):
        """
        Synchronizes the database.

        This method creates receipts in the database for keys that are not found in the database.
        """
        if not self.notFoundInDatabaseKeys:
            return

        receiptRepository = ReceiptRepository()
        dataProvider = DataProvider()
        for key in self.notFoundInDatabaseKeys:
            receiptElement = dataProvider.getkeyFromXMLByKey(key)
            receipt = dataProvider.xmlElementToReceipt(receiptElement)
            receiptRepository.createReceipt(receipt.key, receipt.products)

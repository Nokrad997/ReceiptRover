from src.repositories.TransactionRepository import TransactionRepository
from src.repositories.ReceiptRepository import ReceiptRepository
from src.services.DataProvider import DataProvider


#to nie będzie działac nie używajcie tego nigdzie

class SynchronizationService:
    def __init__(self):
        self.notFoundInLocalKeys = []
        self.notFoundInDatabaseKeys = []
    
    def checkData(self, userId : int) -> bool:
        transactionRepository = TransactionRepository()
        dataProvider = DataProvider()
        
        userKeys = transactionRepository.getUsersTransactionsKeys(userId)
        userlocalKeys = dataProvider.getkeysFromXML()
        self.notFoundInLocalKeys = [key for key in userKeys if key not in userlocalKeys]
        self.notFoundInDatabaseKeys = [key for key in userlocalKeys if key not in userKeys]
        
        if(len(self.notFoundInLocalKeys) != 0 or len(self.notFoundInDatabaseKeys) != 0):
            return False
        
        return True
    
    def synchronizeLocal(self):
        if(len(self.notFoundInLocalKeys) == 0):
            return
        
        receiptRepository = ReceiptRepository()
        dataProvider = DataProvider()
        for key in self.notFoundInLocalKeys:
            receipt = receiptRepository.getReceiptByKey(key)     
            dataProvider.addReceiptToXmlFile(receipt) 
    
    def synchronize_database(self):
        if not self.notFoundInDatabaseKeys:
            return

        receiptRepository = ReceiptRepository()
        dataProvider = DataProvider()
        for key in self.notFoundInDatabaseKeys:
            receiptElement = dataProvider.getkeyFromXMLByKey(key)
            receipt = dataProvider.xmlElementToReceipt(receiptElement)
            receiptRepository.createReceipt(receipt.key, receipt.products)

        



        
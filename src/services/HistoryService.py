from src.services.DataProvider import DataProvider
from datetime import datetime

class HistoryService:
    def __init__(self):
        self.dataProvider = DataProvider()
    
    def getHistory(self):
        receiptArray = self.dataProvider.loadReceiptsFromXmlFile()
        sortedDescendingReceiptArray = sorted(receiptArray, key=lambda receipt: receipt.key[:14], reverse=True)
        dates = self.getDatesFromReceipts(sortedDescendingReceiptArray)
        return sortedDescendingReceiptArray, dates

    def getDatesFromReceipts(self, receipts):
        dates = []
        for receipt in receipts:
            dates.append(datetime.strptime(receipt.key[:14], '%Y%m%d%H%M%S'))
        return dates
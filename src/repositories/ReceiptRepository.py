from src.repositories.Repository import Repository


class ReceiptRepository(Repository):
    def createReceipt(self, key, receiptData):
        query = (
            f'INSERT INTO receipts (key, receipt_data) VALUES ("{key}", "{receiptData}");'
        )
        return self.executeQuery(query)

    def getReceiptById(self, receiptId):
        query = f'SELECT * FROM receipts WHERE receipt_id = {receiptId};'
        return self.executeQuery(query)

    def deleteReceipt(self, receiptId):
        query = f'DELETE FROM receipts WHERE receipt_id = {receiptId};'
        return self.executeQuery(query)

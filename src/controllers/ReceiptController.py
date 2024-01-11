from controllers.DatabaseController import DatabaseController

class ReceiptController(DatabaseController):
    def createReceipt(self, key, receipt_data):
        query = "INSERT INTO receipts (key, receipt_data) VALUES ({key}, {receipt_data});"
        data = (key, receipt_data)
        return self.executeQuery(query)

    def getReceiptById(self, receipt_id):
        query = f"SELECT * FROM receipts WHERE receipt_id = {receipt_id};"
        return self.executeQuery(query)

    def delete_receipt(self, receipt_id):
        query = f"DELETE FROM receipts WHERE receipt_id = {receipt_id};"
        return self.executeQuery(query)
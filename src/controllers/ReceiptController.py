from controllers.DatabaseController import DatabaseController

class ReceiptController(DatabaseController):
    def create_receipt(self, key, receipt_data):
        query = "INSERT INTO receipts (key, receipt_data) VALUES (%s, %s);"
        data = (key, receipt_data)
        return self.execute_query(query, data)
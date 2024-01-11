from controllers.DatabaseController import DatabaseController

class ReceiptController(DatabaseController):
    def create_receipt(self, key, receipt_data):
        query = "INSERT INTO receipts (key, receipt_data) VALUES (%s, %s);"
        data = (key, receipt_data)
        return self.execute_query(query, data)

    def get_receipt_by_id(self, receipt_id):
        query = "SELECT * FROM receipts WHERE receipt_id = %s;"
        data = (receipt_id,)
        return self.execute_query(query, data)

    def update_receipt_data(self, receipt_id, new_receipt_data):
        query = "UPDATE receipts SET receipt_data = %s WHERE receipt_id = %s;"
        data = (new_receipt_data, receipt_id)
        return self.execute_query(query, data)

    def delete_receipt(self, receipt_id):
        query = "DELETE FROM receipts WHERE receipt_id = %s;"
        data = (receipt_id,)
        return self.execute_query(query, data)
    
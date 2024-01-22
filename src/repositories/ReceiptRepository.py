from src.repositories.Repository import Repository


class ReceiptRepository(Repository):
    def createReceipt(self, key, receiptData):
        """
        Create a new receipt in the database.

        Args:
            key (str): The key associated with the receipt.
            receiptData (str): The data of the receipt.

        Returns:
            Any: The result of the database query.
        """
        query = f'INSERT INTO receipts (key, receipt_data) VALUES ("{key}", "{receiptData}");'
        return self.executeQuery(query)

    def getReceiptById(self, receiptId):
        """
        Retrieve a receipt from the database by its ID.

        Args:
            receiptId (int): The ID of the receipt.

        Returns:
            Any: The result of the database query.
        """
        query = f"SELECT * FROM receipts WHERE receipt_id = {receiptId};"
        return self.executeQuery(query)

    def deleteReceipt(self, receiptId):
        """
        Delete a receipt from the database by its ID.

        Args:
            receiptId (int): The ID of the receipt.

        Returns:
            Any: The result of the database query.
        """
        query = f"DELETE FROM receipts WHERE receipt_id = {receiptId};"
        return self.executeQuery(query)

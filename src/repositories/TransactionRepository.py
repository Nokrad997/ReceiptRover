from src.repositories.Repository import Repository


class TransactionRepository(Repository):
    def createTransaction(self, userId, date, scanId, key):
        """
        Create a new transaction record in the database.

        Args:
            userId (int): The ID of the user associated with the transaction.
            date (str): The date of the transaction.
            scanId (int): The ID of the scanned document associated with the transaction.
            key (str): The key associated with the transaction.

        Returns:
            bool: True if the transaction was created successfully, False otherwise.
        """
        query = f'INSERT INTO Transactions (user_id, date, scan_id, key) VALUES ({userId}, "{date}", {scanId}, "{key}");'
        return self.executeQuery(query)

    def getTransactionById(self, transactionId):
        """
        Retrieve a transaction record from the database by its ID.

        Args:
            transactionId (int): The ID of the transaction.

        Returns:
            dict: A dictionary containing the transaction details, or None if the transaction was not found.
        """
        query = f"SELECT * FROM Transactions WHERE transaction_id = {transactionId};"
        return self.executeQuery(query)

    def getTransactionsByUserId(self, userId):
        """
        Retrieve all transaction records associated with a specific user.

        Args:
            userId (int): The ID of the user.

        Returns:
            list: A list of dictionaries, each containing the details of a transaction.
        """
        query = f"SELECT * FROM Transactions WHERE user_id = {userId};"
        return self.executeQuery(query)

    def updateTransactionKey(self, transactionId, newKey):
        """
        Update the key associated with a transaction.

        Args:
            transactionId (int): The ID of the transaction.
            newKey (str): The new key to be associated with the transaction.

        Returns:
            bool: True if the key was updated successfully, False otherwise.
        """
        query = f'UPDATE Transactions SET key = "{newKey}" WHERE transaction_id = {transactionId};'
        return self.executeQuery(query)

    def deleteTransaction(self, transactionId):
        """
        Delete a transaction record from the database.

        Args:
            transactionId (int): The ID of the transaction to be deleted.

        Returns:
            bool: True if the transaction was deleted successfully, False otherwise.
        """
        query = f"DELETE FROM Transactions WHERE transaction_id = {transactionId};"
        return self.executeQuery(query)

    def getUsersTransactionsKeys(self, userId):
        """
        Retrieve the keys associated with all transactions of a specific user.

        Args:
            userId (int): The ID of the user.

        Returns:
            list: A list of keys associated with the user's transactions.
        """
        query = f"SELECT key FROM Transactions WHERE user_id = {userId};"
        return self.executeQuery(query)

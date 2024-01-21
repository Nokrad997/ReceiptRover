from src.repositories.Repository import Repository


class TransactionController(Repository):
    def createTransaction(self, userId, date, scanId, key):
        query = f"INSERT INTO Transactions (user_id, date, scan_id, key) VALUES ({userId}, {date}, {scanId}, {key});"
        return self.executeQuery(query)

    def getTransactionById(self, transactionId):
        query = f"SELECT * FROM Transactions WHERE transaction_id = {transactionId};"
        return self.executeQuery(query)

    def getTransactionsByUserId(self, userId):
        query = f"SELECT * FROM Transactions WHERE user_id = {userId};"
        return self.executeQuery(query)

    def updateTransactionKey(self, transactionId, newKey):
        query = f"UPDATE Transactions SET key = {newKey} WHERE transaction_id = {transactionId};"
        return self.executeQuery(query)

    def deleteTransaction(self, transactionId):
        query = f"DELETE FROM Transactions WHERE transaction_id = {transactionId};"
        return self.executeQuery(query)

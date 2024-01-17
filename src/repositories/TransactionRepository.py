from src.repositories.Repository import Repository

class TransactionController(Repository):
    def createTransaction(self, userid, date, scanid, key):
        query = f"INSERT INTO transactions (user_id, date, scan_id, key) VALUES ({userid}, {date}, {scanid}, {key});"
        return self.executeQuery(query)

    def getTransactionById(self, transaction_id):
        query = f"SELECT * FROM transactions WHERE transaction_id = {transaction_id};"
        return self.executeQuery(query)

    def getTransactionsByUserId(self, user_id):
        query = f"SELECT * FROM transactions WHERE user_id = {user_id};"
        return self.executeQuery(query)

    def updateTransactionKey(self, transaction_id, new_key):
        query = f"UPDATE transactions SET key = {new_key} WHERE transaction_id = {transaction_id};"
        return self.executeQuery(query)

    def deleteTransaction(self, transaction_id):
        query = f"DELETE FROM transactions WHERE transaction_id = {transaction_id};"
        return self.executeQuery(query)
from controllers.DatabaseController import DatabaseController

class TransactionController(DatabaseController):
    def create_transaction(self, user_id, date, scan_id, key):
        query = "INSERT INTO transactions (user_id, date, scan_id, key) VALUES (%s, %s, %s, %s);"
        data = (user_id, date, scan_id, key)
        return self.execute_query(query, data)

    def get_transaction_by_id(self, transaction_id):
        query = "SELECT * FROM transactions WHERE transaction_id = %s;"
        data = (transaction_id,)
        return self.execute_query(query, data)

    def get_transactions_by_user_id(self, user_id):
        query = "SELECT * FROM transactions WHERE user_id = %s;"
        data = (user_id,)
        return self.execute_query(query, data)

    def update_transaction_key(self, transaction_id, new_key):
        query = "UPDATE transactions SET key = %s WHERE transaction_id = %s;"
        data = (new_key, transaction_id)
        return self.execute_query(query, data)

    def delete_transaction(self, transaction_id):
        query = "DELETE FROM transactions WHERE transaction_id = %s;"
        data = (transaction_id,)
        return self.execute_query(query, data)

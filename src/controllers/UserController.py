from controllers.DatabaseController import DatabaseController
import bcrypt

class UserController(DatabaseController):
    def create_user(self, username, password):
        password = self.hash_password(password)
        query = "INSERT INTO users (username, password) VALUES (%s, %s);"
        data = (username, password)
        return self.execute_query(query, data)

    def get_user_by_username(self, username):
        query = "SELECT * FROM users WHERE username = %s;"
        data = (username,)
        return self.execute_query(query, data)

    def get_user_by_id(self, user_id):
        query = "SELECT * FROM users WHERE user_id = %s;"
        data = (user_id,)
        return self.execute_query(query, data)

    def update_user_password(self, username, new_password):
        query = "UPDATE users SET password = %s WHERE username = %s;"
        data = (new_password, username)
        return self.execute_query(query, data)

    def delete_user(self, username):
        query = "DELETE FROM users WHERE username = %s;"
        data = (username,)
        return self.execute_query(query, data)

    def verify_password(self, hashed_password, input_password):
        return bcrypt.checkpw(input_password.encode('utf-8'), hashed_password)

    def hash_password(self, password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password

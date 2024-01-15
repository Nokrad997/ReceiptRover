import psycopg2
import config

class DatabaseController:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                dbname = config.DBNAME,
                user = config.USER,
                host = config.HOST,
                password = config.PASSWORD
            )
            self.cur = self.conn.cursor()

        except Exception as e:
            return e

    def __del__(self):
        self.cur.close()
        self.conn.close()

    def executeQuery(self, query):
        try:
            self.cur.execute(query)
            result = self.cur.fetchall()  
            self.conn.commit()
            return result
        
        except Exception as e:
            return e
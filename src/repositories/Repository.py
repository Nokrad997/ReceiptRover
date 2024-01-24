import psycopg2
import config


class Repository:
    def __init__(self):
        """
        Initializes a new instance of the Repository class.
        Establishes a connection to the PostgreSQL database using the provided configuration.
        """
        try:
            self.conn = psycopg2.connect(
                dbname=config.DBNAME,
                user=config.USER,
                host=config.HOST,
                password=config.PASSWORD,
            )
            self.cur = self.conn.cursor()

        except Exception as e:
            return e

    def __del__(self):
        """
        Closes the database cursor and connection when the Repository instance is destroyed.
        """
        self.cur.close()
        self.conn.close()

    def executeQuery(self, query):
        """
        Executes the given SQL query on the database and returns the result.

        Args:
            query (str): The SQL query to execute.

        Returns:
            list: The result of the query as a list of tuples.

        Raises:
            Exception: If an error occurs during query execution.
        """
        try:
            self.cur.execute(query)
            result = self.cur.fetchall()
            self.conn.commit()
            return result

        except Exception as e:
            return e

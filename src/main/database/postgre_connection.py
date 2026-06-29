from loguru import logger
import psycopg2

class PostgreConnection:
    def __init__(self, config):
        self.config = config
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host=self.config.get('postgre_database', 'host'),
                port=self.config.get('postgre_database', 'port'),
                database=self.config.get('postgre_database', 'database'),
                user=self.config.get('postgre_database', 'user'),
                password=self.config.get('postgre_database', 'password')
            )

            logger.info("Successfully connected to PostgreSQL database.")

        except Exception as e:
            logger.info("Error occurred while connecting to PostgreSQL: {}", e)
            raise e

    def close(self):
        if self.connection:
            self.connection.close()
            logger.info("PostgreSQL connection closed.")

class PostgreCRUDOperations:
    def __init__(self, postgre_connection):
        self.postgre_connection = postgre_connection

    def read_from_postgre(self, query):
        try:
            cursor = self.postgre_connection.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
            return results

        except Exception as e:
            logger.info("Error occurred while executing query: {}", e)
            raise e

        finally:
            cursor.close()

    def write_to_postgre(self, query, data):
        try:
            cursor = self.postgre_connection.cursor()
            cursor.execute(query, data)
            self.postgre_connection.commit()
            logger.info("Data written to PostgreSQL successfully.")

        except Exception as e:
            logger.info("Error occurred while executing query: {}", e)
            self.postgre_connection.rollback()
            raise e

        finally:
            cursor.close()

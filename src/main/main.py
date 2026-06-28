from database.postgre_connection import *
from loguru import logger
import configparser

config = configparser.ConfigParser()
config.read(r'C:\Users\sharm\.vscode\python_programming\src\resources\config_file.ini')

def main():
    postgre_connection_obj = PostgreConnection(config)
    postgre_connection_obj.connect()

    postgre_crud_obj = PostgreCRUDOperations(postgre_connection_obj.connection)

    query = "SELECT winner FROM icc_world_cup"
    results = postgre_crud_obj.read_from_postgre(query)
    logger.info("Query results: {}", results)

    postgre_connection_obj.close()

if __name__ == "__main__":
    main()
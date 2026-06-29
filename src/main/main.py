from database.postgre_connection import *
from loguru import logger
import configparser

config = configparser.ConfigParser()
config.read(r'C:\Users\sharm\.vscode\python_programming\src\resources\config_file.ini')

def main():
    postgre_connection_obj = PostgreConnection(config)
    postgre_connection_obj.connect()

    postgre_crud_obj = PostgreCRUDOperations(postgre_connection_obj.connection)

    read_query = "SELECT winner FROM icc_world_cup"
    results = postgre_crud_obj.read_from_postgre(read_query)
    logger.info("Query results: {}", results)

    write_query = "INSERT INTO icc_world_cup (team_1, team_2, winner) VALUES (%s, %s, %s)"
    data_to_insert = ('India', 'Pakistan', 'India')
    postgre_crud_obj.write_to_postgre(write_query, data_to_insert)

    results = postgre_crud_obj.read_from_postgre(read_query)
    logger.info("Query results: {}", results)

    postgre_connection_obj.close()

if __name__ == "__main__":
    main()
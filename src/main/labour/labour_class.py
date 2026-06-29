from loguru import logger
from src.main.database.postgre_connection import PostgreConnection, PostgreCRUDOperations

import configparser

class Labour:
    total_labourers = 0 # Class variable to keep track of total labourers

    def __init__(self, first_name, last_name, wage, role):
        self.first_name = first_name # Instance variable
        self.last_name = last_name
        self.wage = wage
        self.role = role
        Labour.total_labourers += 1

    def save_to_database(self, crud):
        query = f"SELECT * FROM labour WHERE first_name = '{self.first_name}' AND last_name = '{self.last_name}'"

        result = crud.read_from_postgre(query)
        
        if not result:
            insert_query = "INSERT INTO labour (first_name, last_name, wage, role, email) VALUES (%s, %s, %s, %s, %s)"
            email = self.first_name.lower() + "." + self.last_name.lower() + "@example.com"
            crud.write_to_postgre(insert_query, (self.first_name, self.last_name, self.wage, self.role, email))
            logger.info(f"Labour {self.first_name} {self.last_name} saved to the database.")
        
        if result:
            logger.info(f"Labour {self.first_name} {self.last_name} already exists in the database.")

config = configparser.ConfigParser()
config.read(r'C:\Users\sharm\.vscode\python_programming\src\resources\config_file.ini')

connection_obj = PostgreConnection(config)
connection_obj.connect()

postgre_crud_obj = PostgreCRUDOperations(connection_obj.connection)

labour1 = Labour("John", "Doe", 20.5, "Electrician")
labour1.save_to_database(postgre_crud_obj)

labour2 = Labour("Jane", "Smith", 18.0, "Plumber")
labour2.save_to_database(postgre_crud_obj)

labour3 = Labour("Jack", "Johnson", 22.0, "Carpenter")
labour3.save_to_database(postgre_crud_obj)
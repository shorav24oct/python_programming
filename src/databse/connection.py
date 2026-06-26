from loguru import logger
import psycopg2

connector = psycopg2.connect(
    host="localhost",
    port=5432,
    database="postgres",
    user="postgres",
    password="postgres"
)

cursor = connector.cursor()

logger.info("Executing query...")
cursor.execute("SELECT winner FROM icc_world_cup")

results = cursor.fetchall()
logger.info("Query results: {}", results)

insert_query = "INSERT INTO Labour (first_name, last_name, wage, role, email) VALUES (%s, %s, %s, %s, %s)"
cursor.execute(insert_query, ("John", "Doe", 50000, "Engineer", "john.doe@example.com"))
connector.commit()
logger.info("Inserted new record into Labour table.")

cursor.close()
connector.close()
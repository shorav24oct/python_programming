from loguru import logger

class Labour:
    total_labourers = 0 # Class variable to keep track of total labourers

    def __init__(self, first_name, last_name, wage):
        self.first_name = first_name # Instance variable
        self.last_name = last_name
        self.wage = wage
        Labour.total_labourers += 1

labourer1 = Labour("John", "Doe", 20)
logger.info("Labourer created: {}", labourer1.__dict__)

labourer2 = Labour("Jane", "Smith", 25)
logger.info("Labourer created: {}", labourer2.__dict__)

logger.info("Total labourers: {}", Labour.total_labourers)
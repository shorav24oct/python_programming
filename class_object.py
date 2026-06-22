from loguru import logger

class User:
    def __init__(self, name, age, location=None):
        self.name = name
        self.age = age
        self.location = location

user1 = User("Alice", 30)
logger.info("User created: {}", user1.__dict__)
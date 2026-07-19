import logging

# Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger()

# Functions
def add(a, b):
    result = a + b
    logger.info(f"Addition: {a} + {b} = {result}")
    return result

def subtract(a, b):
    result = a - b
    logger.info(f"Subtraction: {a} - {b} = {result}")
    return result

def multiply(a, b):
    result = a * b
    logger.info(f"Multiplication: {a} * {b} = {result}")
    return result

def divide(a, b):
    try:
        result = a / b
        logger.info(f"Division: {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Cannot divide by zero.")
        return None

# Main Program
if __name__ == "__main__":
    add(10, 5)
    subtract(20, 8)
    multiply(4, 6)
    divide(12, 3)
    divide(10, 0)

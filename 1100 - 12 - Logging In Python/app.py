import logging

## logging settings
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[ 
        logging.FileHandler("app1.log"),
        logging.StreamHandler( )
    ]
)

logger = logging.getLogger('ArithmeticApp')
def add(a,b):
    result = a + b
    logger.debug(f"Adding {a} and {b} gives {result}")
    return result

def subtract(a,b):
    result = a - b
    logger.debug(f"Subtracting {a} and {b} gives {result}")
    return result

def multiply(a,b):
    result = a * b
    logger.debug(f"Multiplying {a} and {b} gives {result}")
    return result

def divide(a,b):
    try:
        result = a/b
        logger.debug(f"Dividing {a} by {b} gives {result}")
        return result
    except ZeroDivisionError as ze:
        logger.error("Zero Division Error")
        return None
    
add(10,5)
subtract(15,10)
multiply(2,3)
divide(2,2)
divide(2,0)
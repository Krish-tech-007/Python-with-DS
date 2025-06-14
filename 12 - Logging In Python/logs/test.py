from logger import logging
def add(a,b):
    logging.debug("The addittion operation is taking place")
    return a+b

logging.debug("The addittion function is being called")
add(10,15)
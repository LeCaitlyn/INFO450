# Caitlyn Le
# INFO 450
# Week 2 - Homework 1

import logging
logging.basicConfig(level=logging.DEBUG)

def squared_threes():
    return_value = []
    numbers = range(3,102,3)
    for value in numbers:
        logging.debug(value ** 2)
    return return_value

if __name__ == "__main__":
    for x in squared_threes():
        print(x)


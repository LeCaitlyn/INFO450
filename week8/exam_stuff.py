
############### Week 1 ###############

# What is logging?
# No Braces, tabs & whitespace!!
# Variables (24) & Variable Types (26)
# Comments
# Strings
# Manipulation of a string
# Stripping (Getting rid of whitespace)
# Formatted strings
# Numbers & Mathematics (Exponents **, Modulus %)
# Multiple Assignments
# Docker

############### Week 2 ###############

# Lists
# Accessing Elements in a list (6)
# CRUD (Create, Read, Update, Delete)
# Appending vs. Inserting (8)
# Deleting (9)
# Sorting (10-11)
# Reverse, length, etc (12)
# Common errors (15)
# Range function (Numerical Lists) (16)
# List Comprehension (18)

############### Week 3 ###############

# Boolean (T/F)
# Conditionals (=,==) ** CASE SENSITIVE (5)
# Inequality (!=) (6)
# Numerical Comparisons (7)
# Multiple conditions (with charts) (8)
# Checking lists (in/not in) (9)
# Simple if statements (10)
# Is list empty? (14)
# Multiple Lists (pizza example) (15)

############### Week 4 ###############

# Dictionaries (syntax--alien example) (4)
# Creating (key, value) (5)
# Modifying data
# Using .get to access data (7)
# Dictionary Functions (10)
# Looping (TV example) (11)
# Only output unique values (loop) (12)

############### Week 5 ###############

# Files
# File operations (4)
# Writing data to files (append) (6)
# Reading the data back (8)
# Using JSON to make it prettier (10-11)
# .csv files (12)
# Iliad example (13)
# Word count and frequency Example Code (16)

############### Week 6 ###############

# None (3)
# Load and dump JSON (4)
# Functions Overview (5)
# Function to print a help menu (7)
# Fibinachi example (parameters) (8-9)
# Multiple parameters (10)
# Optional parameters (11)
# Mix and Match Parameters (12-13)
# Returning values from a function (dogtype) (14)
# Empty return statements are essentially none (15)
# Returning multiple values (16)
# Syntax errors (18)
# Exceptions (19)
# Handling exceptions (20)
# Fake number example (21)
# Cleanup actions (executed under all circumstances) (24)
# Command line arguments (25)

############### Week 7 ###############

# Numpy

# 1. False
# 2. 'foo\'bar'
# 3. print("Hello World!")
# 4. #
# 5. No answer?
# 6. __name__
# 7. .py
# 8. 1
# 9. float
# 10. 3 if we assign the value to a variable and then "print" the variable; otherwise nothing will appear in the STOUT.
# 11. Insert, append
# 12.

# import logging
# logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

# def list_printer(my_list=None):
#     if not my_list:
#         print("Just kidding, my list is empty...")
#     else:
#         for x in my_list:
#             print(x)


# if __name__ == "__main__":
#     logging.debug("Here is my list:")
#     list_printer(my_list = ['1','2','3','4'])
#     logging.debug("Here is my list:")
#     list_printer()
#     logging.debug("Here is my list:")
#     list_printer(None)
#     logging.debug("Here is my list:")
#     list_printer([])
#     logging.debug("Here is my list:")
#     list_printer(my_list = ["a",'b',3])

# 13. 

# car = {}
# car = {"Number of Doors" : 4, "Weight" : 3680, "Color" : "Rhino Gray"}
# print("The number of doors for this car is", car["Number of Doors"])
# print("The car is", car["Weight"], "pounds")
# print("The car is a beautiful", car["Color"])

# 14. f
# 15. ndarray
# 16. The output would be an array containing the list of numerical values from 0 to 14. 
#     So: array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14])
# 17. False
# 18. 1
# 19. Python takes all of the values from the function and puts them into a tuple (a tuple of (1, 2, 3) 
#     in this case). Then, in line 4, we assign each of the values in the tuple to a variable. By using 
#     the underscore, we are deciding to not assign the first and second (2, 3) values in the tuple. Therefore, 
#     since only our zeroth value (1) is assigned a variable (x), we leave the first and second values in the 
#     tuple behind and they are not printed. The underscores are necessary for Python to know we do not want to 
#     assign 2 and 3 to variables.
# 20. Always close your files after you open them!!! Computers have limits, just like people. If there are too 
#     many files open on your OS, it is possible that your computer will crash. Your program will also crash, 
#     and other bad things could happen. Don't lose your work, close your files!
# 21. Except
# 22. Runtime
# 23. Compile Time
# 24. 

import logging
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

def find_runner_up(score_list=None):    
    last_list = []      
    score = []

    if len(score_list) > 2:        
        new_list = score_list.sort()        
        new_list_2 = score_list.sort()        
        for x in new_list:            
            if x not in new_list_2:                
                last_list.append(x)        
        return last_list

    elif len(score_list) < 1:        
        print("There is no runner up.")   

    else:   
        print("There is a tie!")            
        
    last_list = sorted(last_list)    
    score = last_list[-2]

    return(score) 

if __name__ == "__main__":   
     find_runner_up(score_list=[1, 2, 3, 4, 5, 5, 5, 5, 5])
#debugging is the process of identifying and removing errors from computer hardware or software. it is a critical skill for developers to ensure their code runs smoothly and efficiently. here are some common techniques and tools used for debugging in python:

#using print function and F-strings
def divide_numbers(a, b):
    result = a/b
    print(f"dividing {a} by {b} gives {result}")
    return result

#we can use the pdb module

import pdb

def divide_numbers_with_pdb(a, b):
    pdb.set_trace()  # set a breakpoint here
    result = a / b
    return result 


divide_numbers_with_pdb(10, 0)  # this will raise a ZeroDivisionError

def divide(a, b):
    result = a / b
    return result

print(divide(10, 2))
print(divide(15, 3))
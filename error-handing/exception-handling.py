#exception handling allows you to anticipate and manage errors in your code gracefully. here are some common techniques for handling exceptions in python:

#using try and except blocks
def divide_numbers(a, b):
    try:
        result = a/b
        print(f"dividing {a} by {b} gives {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    
#doing the try, else , except and finally
def divide_numbers_with_finally(a, b):
    try: 
        result = a/b
        print(f"dividing {a} by {b} gives {result}")
    except ZeroDivisionError:
        print("Error: cannot divide by zero")
        return None
    else:
        print("Division successful.")

    finally:
        print("Execution of divide_numbers_with_finally is complete.")

divide_numbers_with_finally(10, 2)
divide_numbers_with_finally(15, 0)
#a raise statement is used to manually trigger an exception in python. it is useful when you want to enforce certain conditions in your code and signal that error has occurred. here are some of the common ways to use the raise statement":

def checL_age(age):
    if age < 0:
        raise ValueError("age cannot be negative")
    elif age < 18:
        raise ValueError("Age must be at least 18 to register")
    
try:
    checL_age(-5)
except ValueError as e:
    print(e)
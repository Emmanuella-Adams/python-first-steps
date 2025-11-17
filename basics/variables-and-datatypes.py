#Hi!! so this basically is just me getting the hang of learning python

#complex
my_complex_var = 3 + 1j
print('This is a complex variable', my_complex_var)

#set
my_set_var = {1, 2, 3, 5, 7, 8 }
print('This is my Set variables', my_set_var)

#dictionary
my_dictionary_var = {'name :' 'Alice', 'age:' '18'}
print(my_dictionary_var)
my_dictionary_var = {'name' : 'Alice', 'age' : 10}
print(' this is my dictionary variable', my_dictionary_var)

#tuple
my_tuple = ( 7, 3, 2, 6)
print('this is a tuple', my_tuple)

#list
my_list = [22, 'mother', True, 0.124]
print('this is a list', my_list)

#none
my_none = None
print('my none variable', my_none)

#this prints out the variable
print(type(my_complex_var))
print(type(my_set_var))

#isinstance compares a variable to a datatype and returns True if it matches, otherwise False
print(isinstance('i love food', str))
print(isinstance(my_set_var , set))

#to identity for easy understanding and documentation
username : str = 'john doe'


def greet (name : str , age : int) -> str:
    return f'hello, {name}, age {age}'

username : str = 'john doe'
userage : int = 14

print(greet (username, userage))

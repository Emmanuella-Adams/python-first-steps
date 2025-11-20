#scope in python follows the LEGB rule

#Local scope (L): Variables defined in functions or classes.

#Enclosing scope (E): Variables defined in enclosing or nested functions.

#Global scope (G): Variables defined at the top level of the module or file.

#Built-in scope (B): Reserved names in Python for predefined functions, modules, keywords, and objects.



def see():
    my_see = 55
    print(my_see) #my_see is a local variable

see()

#Enclosing scope means that a function that's nested inside another function can access the variables of the function it's nested within.
#lets enclose a function 

def senses():
    eyes = 'see'
    print('eyes are used to', eyes)

    def colors():
        colours = 'the colors of the rainbow'
        print(colours)

    colors()

senses()

#Global scope refers to variables that are declared outside any functions or classes which can be accessed from anywhere in the program

body = ['head', 'shoulders', 'knees', 'toes'] #this is a global scope

def upper_body():
    print(body[0] , 'and' , body[1], 'are the upper body') #we are using our global list inside our local function

def lower_body():
    print(body[2] , 'and' , body[3], 'are the lower body')

upper_body()
lower_body()

print('never the less, they are all part of your body')

#You can also use the global keyword to modify a global variable:

def modify():
    global body
    body = ['eyes', 'ears', 'nose' , 'mouth'] #this modifies our global variable
    print(body)

modify()

#built-in scope refers to all of Python's built-in functions, modules, and keywords, and are available anywhere in your program:
print('hello')
print(str(23932))
print(type(False))
print(isinstance(3 , int))
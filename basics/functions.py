#unctions are reusable piecies of code that function when you call them

#lets start with the function input()

name = ''' input(' what is your name? ')
location = input(' where did you come from? ')

print('ah,' , name , 'it\'s nice to meet you, i\'ve heard a lot about' , location ) '''

#int() it converts  number, boolean, and a numeric string into an integer:
print(int(5.22))
print(int('3934234'))
print(int(False))

#To call on a custom function, you do this with def function_name ():

def questions():
    print('hello world')

#if you want  to call on the functions
questions()

def summation(a , b):
    our_sum = a + b
    print(our_sum)
    
print(summation(3, 4)) #this shows none because we didn't use the 'return' keyword

def subtraction(c , d):
   our_sub = c - d
   return(our_sub)

print(subtraction(3, 4)) #this shows none because we didn't use the 'return' keyword
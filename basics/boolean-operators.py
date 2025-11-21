#if you want to check if your value is ture or false, you use the bool(value)

print(bool(False))
print(bool('nigeria'))
print(bool(24))
print(bool(4324.233424))

#There are three Boolean operators in Python: and, or, and not.

#first of all, we take a look at the and operator
age = int(input('whats your age? integers only '))
height = int(input('how many cm are you in height? '))

if age >= 18 and height <= 180:
    print('goodness me, youre an adult')

else:
    print('getout')

    #lets look at the or operator with the same perspective
or_age = int(input('whats your age? integers only '))
or_height = int(input('how many cm are you in height? '))

if or_age >= 18 or or_height <= 180:
    print('goodness me, youre an adult')

else:
    print('getout')

#we have the not operators

print(not '') #true
print(not 55) #false
print(not False) #true
print(not 'chimi') #false

#lets try it in admin form

is_admin = False


if not is_admin:
    print('you are not an admin, go back to the main page')

else:
    print('welcome admin, it\'s good to have you back, hope you didn\'t lie')
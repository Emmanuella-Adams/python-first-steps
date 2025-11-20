#Conditional statements, or conditionals, let you control the flow of your program based on whether certain conditions are true or false.
print(2>3)
print(2<3)
print(2==3)
print(2>=3)
print(2<=3)
print(2!=3)
#these presents either true or false factors

#In Python, the most basic conditional is the if statement.

eyes = input('how many eyes do you have? ')
eyes = int(eyes)

if eyes != 2:
    print('youre a monster! how could you have' , eyes , 'eyes?!')

else:
    print('phew! that was close!')


#we can also use elif since we want to do much okay?

age = input('how old are you, i wanna marry you ')
age = int(age)

if age > 18:
    print('good, youre a perfect match')

elif age == 18:
    print('youre a bit young, though its technically legal')

else:
    print('shoo litle one! go back to school')
#tuples are a puthon data types, they can conntain a mixed set of groups, they are marked by two (), tuples are immutable, meaning they cannot change, be deleted of modified 
emmanuella = ('178 cm', 19 , 'software Engineer')

#to acess the element in the tuple, you open with a []
print(emmanuella[2])

#you can also check whether an element is inside a turple
print(19 in emmanuella) #it gives out true value
print('javascript' in emmanuella) #gives out the truth value

#you can also unpack like you did with the lists
height, age, proffession = emmanuella
print(height) #178cm

#you can also add the *rest value
food = ('rice', 'beans', 'curry', 'meat', 'eggs')
I_like, *rest = food
print(I_like)
print(rest)

#you can also slice it
print(food[1:3])
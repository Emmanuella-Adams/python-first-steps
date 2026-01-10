# you can basicaly change sets, and stuff. so lets go
my_set = {1 , 3 , 'setty' , 3.232323 }

#if you need to define an empty set, you need to do this
set() #set
{} #dictionary

#you can ad elements like this

my_set.add(4953945)
print(my_set)

#the thing is that we can also add the same thing and nothing will change.

my_set.add('setty') #see, no change ;)

print(my_set)
#if we want to get rid of one stuff, i mean element, we can use two main methods .discard() and .remove() - which raises a keyeror when not found

my_set.remove('setty')
print(my_set)

#.clear() removes all the elements on the set
my_set.clear()
print(my_set) #the shi returns set() empty

#alright were going to go to subset and superset
food = { 'junk food' , 'vegetables' , 'fruits' , 'grains' , 'tubers'}

good_food = { 'vegetables' , 'fruits' , 'grains' , 'tubers'}

#now were gonna check if our set is a subset of another set, and it wil give an answer

print(good_food.issubset(food)) #it gives a true
print(food.issuperset(good_food)) #it gives a true

print(good_food.issuperset(food)) #it gives a false
print(food.issubset(good_food)) #it gives a false

#now we wil check if two points are disjointed
print(good_food.isdisjoint(food)) #it gives a false
print(good_food.isdisjoint(my_set)) #it gives a true

#we can do union and intersection as well
print(food.union(good_food)) #it gives all the elements without repeating

print(food.intersection(good_food)) #it gives only the elements that are in both sets
print(food.difference(good_food)) #it gives only the elements that are in food but not in good_food

# my_set | your_set is the same as my_set.union(your_set)
# my_set & your_set is the same as my_set.intersection(your_set)
# my_set - your_set is the same as my_set.difference(your_set)

your_set = {'soda', 'candy', 'fruits'}
print(food | your_set) #union
print(food & your_set) #intersection

print(food - your_set) #difference

my_set ^ your_set # {1, 5, 6} is the same as my_set.symmetric_difference(your_set)
print(my_set ^ your_set) #symmetric difference
#symmetric difference gives the elements that are in either set, but not in both

#|= &= -= ^= are the same as update methods
my_set |= your_set
print(my_set) #it adds the elements of your_set to my_set
my_set &= your_set
print(my_set) #it keeps only the elements that are in both sets
my_set -= your_set
print(my_set) #it removes the elements of your_set from my_set
my_set ^= your_set
print(my_set) #it keeps only the elements that are in either set, but not in

print(5 in my_set) #it checks if there is an element in your set, returning either true or false
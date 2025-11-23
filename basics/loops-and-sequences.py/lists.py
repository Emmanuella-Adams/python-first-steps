#The list data type is an ordered sequence of elements that can be comprised of strings, numbers, or even other lists. Similar to JavaScript, lists are mutable and use zero-based indexing, meaning that the first element of the list is at index zero.

#we can use the indexes to get the specific  thing we want from the list
colors = ['red', 'blue', 'green', 'yellow', 'purple']
food = ['rice' , 'garri' , 'beans' , 'yam' , 'plantain']
print(food[3])

#even the negstive indexes
print(colors[-1])

#we can also create a list using the list constructor list()
name = 'emmanuella'
name_list = list(name)
print(name_list)

foodie = 'i love food'
foodie = list(foodie)
print(foodie)

#we can also update the list 
colors[-1] = 'maroon'
print(colors)

#if we want to remove an element from the list, we use del keyword
del food[2]
print(food) #beans was ommited

#we can nest list inside list
food[3] = ['carbohydrates', 'fat and oil', 'protein', 'mineral salts']
print(food)

#we can also cal the nested list like this
print(food[3][2]) #peotein

#we can check if an element is inside a list
'yam' in food #true
'chicken' in food #false

#but ofcourse we can use this
print('yam' in food)

#we can assign and unpack values like this
like , hate , neutral , toxic = food[3]
print(like) #carbohydrates
print(toxic)

#if we need to rename the rest of the elements in the list, we use asterisks
favourite_color ,   *indifferent = colors
print(favourite_color)
print(indifferent)

#we have the slice operator whic does this
countries = ['Nigeria', 'algeria', 'togo', 'france', 'USA']
print(countries[1:3])

#we can also choose which step interval we want to do
print(countries[0::2]) # it shows nigeria, togo and usa
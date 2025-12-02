#below are some of the known methods for tuple

#count() used  to count how many times an element appears in a tuple
food = ('rice', 'beans', 'pepper', 'curry', 'yam', 'potatoes', 'yam')
print(food.count('yam'))

#index is usex to find the index of an eement in a tuple
print(food.index('curry')) #retuns 3

# you can also have a start and stop index, which ever you choose
print(food.index('yam', 4, 6 ))

#sorted is for arrianging numbers
number = 2, 56, 354, 21, 435, 3467, 223, 546, 54
print(sorted(number))

#we can also do this according to the length of the string
print(sorted(food , key=len))

#we can also do reverse 
print(reversed(number))
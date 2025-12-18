#The range() function is used to generate a sequence of integers. Here is the basic syntax for the range() function:

for num in range(1, 5):
    print(num)

#same with increment, we use this shii range(start , stop , step)

#in here, we increase so that there are only even number, meaning we increased by two steps
for letter in range(0 , 11 , 2):
    print(letter)

#we can use a negative step integer
for letter in range(0 , 11 , -10):
    print(letter)
#we're gonna look at methods of lists like append(), pop(), and sort()

#append() is used to ard an element to the end of a list
numbers = [1, 2, 3, 4, 5, 6]
numbers.append(7)
print(numbers) #prints [1, 2, 3, 4, 5, 6, 7]

#if you want to add the list to another
even_numbers = [2, 4, 6]
numbers.append(even_numbers)
print(numbers) #prints [1, 2, 3, 4, 5, 6, 7, [2, 4, 6] ], which keeps the []

#if you want to do the same without the stuff [], we use extend()
odd_numbers = [1, 3, 5, 7]
numbers.extend(odd_numbers)
print(numbers) #prints [1, 2, 3, 4, 5, 6, 7, [2, 4, 6], 1, 3, 5, 7]

#to insert as a specific index, we use insert()
worder = 'are even numbers while this are odd numbers:'
numbers.insert(8, worder)
print(numbers) #prints [1, 2, 3, 4, 5, 6, 7, [2, 4, 6], 'are even numbers while this are odd numbers:',  1, 3, 5, 7]

#If you want to remove an element from a list, you can use the remove() method
numbers.remove(1)
print(numbers)  #prints [2, 3, 4, 5, 6, 7, [2, 4, 6], 'are even numbers while this are odd numbers:',  1, 3, 5, 7], it only removes the first occurence of the element

#To remove an element at a specific index in the list, you can use the pop() method like this:
numbers.pop(7)
print(numbers) #prints [2, 3, 4, 5, 6, 7, [2, 4, 6],  1, 3, 5, 7]

#if we want to empty the list, we use clear()
numbers.clear()
print(numbers) #returns an empty list

add_numbers = [ 1, 3, 445, 245, 85, 432, 53, 2, 899  ]
numbers.extend(add_numbers)
print(numbers)

#if we want to sort our list from the smallest to the biggest we use sort()
numbers.sort()
print(numbers)

#In contrast to the sort() method, there is the sorted() function which works for any iterable and returns a new sorted list instead of modifying the original list. For example
unsorted_numbers = [ 1, 3, 445, 245, 85, 432, 53, 2, 899  ]
sorted_numbers = sorted(unsorted_numbers)
print(sorted_numbers)

#The next method we will take a look at is the reverse() method. This method, will reverse a list of elements in place like this:
sorted_numbers.reverse()
print(sorted_numbers)

#The last method we will take a look at is the index method. This is used to find the first index where an element can be found in a list. Here is an example of using the index method to find the language 'Java' in a programming_languages list:
print(sorted_numbers.index(2))

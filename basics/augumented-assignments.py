#Augmented assignment combines a binary operation with an assignment in one step. It takes a variable, applies an operation to it with another value, and stores the result back into the same variable.

#its basically the same thing as variable <operator>= value

#addition
add_variable = 22
add_variable += 5
print(add_variable) #the answer is 27, it is much easier to do than just doing variable = variable + 5

#subtraction
sub_variable = 22
sub_variable -= 5
print(sub_variable) #the answer is 17

#multiplication
mul_variable = 22
mul_variable *= 5
print(mul_variable) #the answer is 110

#division
div_variable = 22
div_variable /= 5
print(div_variable) #the answer is 4.4

#floor division
floor_div_variable = 22
floor_div_variable //= 5
print(floor_div_variable) #the answer is 4

#modulus
mod_variable = 22
mod_variable %= 5
print(mod_variable) #the answer is 2

#we have the exponential assignment operators
div_variable = 22
div_variable **= 5
print(div_variable) #the answer is 5153632


#we also have those for augumented assignments operators, like those for bitwise oprators that include &=, ^=, >>=, and <<=.

#using assignment operators with strings

#addition
add_string = 'hello'
add_string += 'world'
print(add_string) #the answer is helloworld, it is much easier to do than just doing string = string + 'world'

#multilication, maybe to do a string a certain amount of time
#addition
mul_string = 'hello'
mul_string *= 3
print(mul_string) #the answer is hellohellohello

#however, other auguments throw a type error

#if you're wondering if increment and decrement operators (++ and  --) work in Python, they don't. That's because Python deliberately avoids C-style increment and decrement shortcuts in order to keep the language clear and explicit.

#Instead of x++, you can simply write x += 1, which makes it obvious that you're incrementing the value of x by 1.

#Writing ++x in Python just applies the unary plus twice, and increment anything:

my_var = 5

print(+my_var)   # 5
print(++my_var)  # 5, did you see the error sign? yeah, i guess you did
print(+++my_var) # 5

my_var += 1

print(my_var) # 6
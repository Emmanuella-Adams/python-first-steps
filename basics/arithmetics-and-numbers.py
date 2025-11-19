#this is the arithmetic side of pthon, which well be working with most of the time

#lets start with integers

#integers
my_int = 50
my_int2 = 30


print('the addition of the first and second integer is' , my_int + my_int2)

#float
my_float = 3.12
my_float2 = 2.22

print('the addition of the first and second float is' , my_float + my_float2)

#addition
add_int = my_int + my_int2
print(add_int , ' is the addition of the integers')

add_float = my_float + my_float2
print(add_float , ' is the addition of the floats')

#subtraction
sub_int = my_int - my_int2
print(sub_int , ' is the subtraction of the integers')

sub_float = my_float - my_float2
print(sub_float , ' is the subtraction of the floats')

#multiplication
multi_int = my_int * my_int2
print(multi_int , ' is the multiplication of the integers')

multi_float = my_float * my_float2
print(multi_float , ' is the multiplication of the floats')

#division, every division ends with floats
div_int = my_int / my_int2
print(div_int , ' is the division of the integers')

div_float = my_float / my_float2
print(div_float , ' is the division of the floats')


#modulus
mod_int = 9
mod_int2 = 2

mod_float = 23.2
mod_float2 = 11.1

modulus_int = mod_int % mod_int2
print(modulus_int , ' is the modulus of the integers')

modulus_float = mod_float % mod_float2
print(modulus_float , ' is the modulus of the floats')

#floor_division, divides two numbers and returns the greatest number less than or equal to the result
floor_int = 9
floor_int2 = 2

floor_float = 23.2
floor_float2 = 11.1

floor_division_int = floor_int // floor_int2
print(floor_division_int , ' is the floor_division of the integers')

floor_division_float = floor_float // floor_float2
print(floor_division_float , ' is the floor_division of the floats')

#converting to float using float()
int1 = 34
convert_int = float(int1)

print(convert_int , ' is the conversion of' , int1 , 'to float')

#converting to integer using int()
float1 = 245.23
convert_int = int(float1)

print(convert_int , ' is the conversion of' , float1 , 'to integer')

#rounding a decimal to an integer or specific length using round()
roundee1 = 34.34445
roundee2 = 2.934841

round_up1 = round(roundee1) #normally to integer without remainder
round_up2 = round(roundee2 , 1) #rounding up to 1 decimal

print(round_up1 , 'is rounding' , roundee1 , 'to an integer')
print(round_up2 , 'is the rounding' , roundee2 , 'to 1 decimal')

#finding the absolute value of numbers
abstract1 = -34.34445
abstract2 = -2

abstraction1 = abs(abstract1)
abstraction2 = abs(abstract2) 

print(abstraction1 , 'is finding the absolute value of' , abstract1 )
print(abstraction2 , 'is finding the absolute value of' , abstract2 ,)

#converting an integer to a binary using bin()
binary_og = 22
binary = bin(binary_og)
print(binary , 'is the binary representation of' , binary_og)

#converting an integer to a octal using oct()
octal_og = 22
octal = oct(octal_og)
print(octal , 'is the octal representation of' , octal_og)

#converting an integer to a hexadecimal using hex()
hexadecimal_og = 22
hexadecimal = hex(hexadecimal_og)
print(hexadecimal , 'is the hexadecimal representation of' , hexadecimal_og)

#finding the power using pow() or **

result = pow(2,3) 
result2 = 2**3

print(result, 'and' , result2 , 'is the result of two raised to the power of three, irregardless of the method chosen')
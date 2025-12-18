numbers = [1, 2, 3, 4, 5]

def square(num):
    return num ** 2

squared_numbers = list(map(square, numbers))
print(squared_numbers) # [1, 4, 9, 16, 25]

def calculate_expression(x):
    if x > 0:
        return x**2 + 2*x - 1
    else:
        return x**3 - x + 4

print(calculate_expression(3))  # 14

numbers = [1, 2, 3, 4, 5]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4]

numbers = [1, 2, 3, 4, 5]

square = lambda x: x ** 2
squared_numbers = list(map(square, numbers))
print(squared_numbers) # [1, 4, 9, 16, 25]
products = {

    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}

'''#The .values(), .keys(), and .items() methods are essential for these techniques.

#values() is for revealing the values
for price in products.values():
    print(price) 

#key() is for printing the key in the dictionary

for product in products.keys():
    print(product)

#items() is like to state both of them
for item in products.items():
    print(item)

#Now that you know more about this, we can go back to our initial example. If we want to offer a 20% discount, we would multiply each price by 0.8 and reassign it as the value of that product key.

price = products.items()

for products, product in products.items():
    products[product] = round(price * 0.8)

    print(product)'''

for enumerated in enumerate(products):
    print(enumerated)

#If you need to iterate over the values, you can replace products by products.values():
for price in enumerate(products.values()):
    print(price)

    #you can separate the loop variables as well

    for index, price in enumerate(products.values()):
        print(index, price)
        
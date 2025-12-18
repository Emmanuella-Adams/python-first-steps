#we'll first go through the first loop

color = ['red', 'blue', 'lavender', 'pink', 'purple', 'green', 'yello', 'brown']

for char in color:
    print(char)


programming_languages = ['Rust', 'Java', 'Python', 'C++']

for language in programming_languages:
    print(language)

categories = ['Fruit', 'Vegetable']
foods = ['Apple', 'Carrot', 'Banana']

for category in categories:
    for food in foods:
        print(category, food)


words = ['mage', 'tank', 'lead', 'cyst', 'assasin', 'hero', 'analyst', 'Rhythm', 'myth']

for word in words:
    for letter in word:
        if letter.lower() in 'aeiou': 
             print(f'{word} has {letter} in it')
             break

        else:
            print(f'{word} has no vowel in it')

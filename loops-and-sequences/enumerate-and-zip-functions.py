#okay, so we just do this

languages = ['spanish', 'english' , 'french', 'korean', 'igbo' , 'chinese', 'japanese']

for lanugage in languages:
    print(languages)

#if we want to keep track of each indent we do this

index = 0

for language in languages:
    print(f'Index {index} and language {language}')
    index =+ 1

#The best way to do it is to enumerate()

list(enumerate(languages))

#lets try this
color = ['pink', 'blue', 'green', 'red', 'black', 'brown', 'purple' ]

for index, color in enumerate(color, 1):
    print(f'Index {index} and color{color}')

#if we want to join two or more lists together
print(list(zip(languages , color)))

developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]

for name, id in zip(developers, ids):
    print(f'Name: {name}')
    print(f'ID: {id}')
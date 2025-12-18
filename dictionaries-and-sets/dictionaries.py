#dictionaries in pyhton is basically more like the real thing. example

meanings = {
    'noun' : 'name of a person, animal place or thing',
    'verb' : 'an action word, or doing word',
    'adverb' : 'a word  that modifies a verb',
    'types_of_figures_of_speech' : 1,
    'names_of_figures_of_speech': ['noun' , 'verb' , 'adverb']

}

#another alternative is using the dict constructor dict()

buns = dict([('base' , 'flour') , ('oil' , 'vegetable oil') , ('amount' , 1) , ('ingredients' , ['flour' , 'oil' , 'egg' , 'milk' , 'sugar' , 'butter'])])

#if we want to access the keyword for the stuff, we use the dictionart[name] path

print(meanings['noun'])

print('the ingredients for buns are:\n' , buns['ingredients'])

#The .get() method retrieves the value associated with a key. dictionary.get(key, default)
print(buns.get('base' , []))  #this returns an empty list if it isnt found rather than an error

#The .items() method returns a view object with all the key-value pairs in the dictionary, including both the keys and the values:

print(buns.items())

#the clear method  clears all the things from the list but im affraid to do that so ill just safely put it in a function xD
def clearation(dictionary):
    
    cleared = dictionary.clear()
    return cleared

print(clearation(buns))

print(clearation(meanings))

#this is if you just wanna get rid of one
buns.pop('amount' , 1)

#if you want to update, you simply just use the .update() function

buns.update('amount' , 1)


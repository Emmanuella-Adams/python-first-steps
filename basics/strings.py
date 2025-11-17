#so i am using this to learn all about strings, lets goo!!


#it doesnt matter if its " " or ' ' bit it must be the same at the beginning and end
my_str = 'Hello World'
print(my_str)

#we can also have multiple lines of strings
my_str_ml = '''

so this is a multi line string and its actually so much funn
you feel me?'''
print(my_str_ml)

#so actually, we cant just print normally with quotes inside the quotes, instead, we do this
msg = " it's a nice message" # you see that? dont make them similar
msg2 = ' and emmanuella cried, "Eureka!!"' #see this too? that's how you do it

#if you dont want to do the one above you can just do this instead
msg3 = 'it\'s not a nice message'
msg4 = "all in all, she screamed \"I love Python!!\", later she then said, \" just kidding\""

#to combine strings we just do this
print(msg + " " + msg2) # they only work with strings so dont try anything funny

#we can also use this little guy +=
msg4 += msg3
print(msg4) #this is our result

#if we wanna convert this shii to string we do this
hehe = 3429595
#lets check
print(type(str(hehe)))

# so we use the f word now. jk its very easy to use
name = 'Emmanuella'
age = 18
about_me = f'this is {name}, she really is a jet2 holiday. and she\'s only {age} years old'
print(about_me)

#if we want to find the chiggas that are inside. the numbers starting from 0, we do this shii
typeshii = 'a jet2 holiday'
print(len(typeshii))

#if you wanna find the index
print(typeshii[3])
print(typeshii[12])

#to find the negative index
print(typeshii[-5])
print(typeshii[-3])

#now to slice and dice our string with this bomination string[start : stop]
print(typeshii[2 : 5 ]) #we get jet
print(typeshii[5 : ]) # we get 2 holiday
print(typeshii[ : 5]) # we finally get a jet

#we have this monstrosity. the extra is to skip the shii we dont need. string[start : stop : step ] the step shii is to skip the letters 
hopscotch = typeshii[2 : 13 : 2] # the 1 is to skip the 1 in every index, and we get
print(hopscotch) #jt oia, complete nonsense, but atleast it works

#if we wanna do dr strange typeshii, we go reverse
dr_strange_typeshii = typeshii[ : : -1] #hehe
print(dr_strange_typeshii)

#alright we wanna check if typeshii has some words or set of words in it, itll give us true or false depending on what we put
print('jet2' in typeshii) #this is true, i guess
print('shii' in typeshii) #false
print('3' in typeshii) #false
print('ho' in typeshii) #true
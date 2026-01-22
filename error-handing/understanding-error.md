When writing Python code, it's common to run into errors. Understanding these errors is key to debugging your code quickly and efficiently. These messages tell you exactly what went wrong, if you know how to read them.

Common Python errors include SyntaxError, NameError, TypeError, IndexError, and AttributeError. These occur when Python doesn't understand your code, or when your logic doesn't match the data you're working with.

### SyntaxError: this is when a code doesnt follow the proper syntax rules.

```
print('Hello world"
#this is a syntax error

```

### NameError: this is when you input the name of a variable that hasnt been found yet

```
print(name)
#name hasnt been defined so its a NameError

```

### TypeError: this has to do with datatypes and their incompatibility to some operations

```
5 + 'red'
#this will raise a TypeError, a string cannot be concatenated with an integer

```

### Index error: this is an index that doesnt exist in the list

```
color = ['white' , 'black' , 'pink' , 'blue']
print(color[4])
#this will raise an IndexError because the index stops at [3]

```

### Attribute error: this is the type of error that occurs when you try to use a method or property that doesnt exist in that same datatype.

```
num = 22
num.append()
#this will raise an AttributeError because there is no way an integer can append

```



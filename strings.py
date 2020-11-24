# multiline strings
a = '''Lorem ipsum dolor sit amet, 
consectetur adipiscing elit. 
Etiam blandit ac velit quis vehicula. 
Nulla facilisi. Donec vel justo nibh. 
Maecenas consectetur tellus nibh.'''
print(a)

# strings are arrays
a = "Hello World"
print(a[1])

# slicing
a = "Hello World"
print(a[1:5])

b = "Hello World"
print(b[-5:-1])

#String Length
a = "Hello World"
print(len(a))

# Strip() removes any whitespace from the beginning or the end
a = " Hello World "
print(a.strip())

# lower() method returns the string in lower case
a = 'Hello World'
print(a.lower())

# upper() method replaces a string with another string
a = "Hello World"
print(a.upper())

# replace() method replaces a string with another string
a = "Hello World"
print(a.replace("W", "V"))

# Check String
txt = "Python is awesome programming languange"
x = "awe" in txt
print(x)

# String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

# String Format
age = 20
txt = "My name is Kevin, I am {}"
print(txt.format(age))

color = "yellow"
type = "fruit"
txt = f"The Banana {color} is {type}"
print(txt)

# Escape Character
txt = "Django is framework \"python\" "
print(txt)

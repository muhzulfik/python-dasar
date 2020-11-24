# creating a function
def my_function():
    a = 20
    b = 'Hello from a function {}'
    print(b.format(a))

# calling a function
my_function()

# Argument
def my_hero(fname):
    print(fname + ' marvel')

my_hero('thor')
my_hero('iron man')

# Arbitary Arguments

def my_name(*kids):
    print("The youngest child is " + kids[0])

my_name("Suep", "Jaja")

# keyword argumments
def my_function(child3, child2, child1):
    print('The youngest child is' + child3)

my_function(child1 = "Emil", child2 = 'suep', child3 = 'japrak')

# Passing a List
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# Return Values
def my_function(x):
    return 5 * x

print(my_function(3))

# Rekursif

def rekursif(angka):
    if angka > 0:
        print(angka)
        angka = angka - 1
        rekursif(angka)
    else:
        print(angka)
masukan = int(input())
rekursif(masukan)

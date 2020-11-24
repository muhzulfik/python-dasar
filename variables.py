# variables
a = 10 # a is variables
print(a)

a , b, c = "banana", "grape", "apple"
print(a, b, c)
print(a, "is a fruit")
print(a + " and " + b + " is same fruit")

def myfunc():
    a = "starfruit" #localvaribles
    print("yellow identic with " + a )

myfunc()
print("yellow identic with " + a ) #used a global variables

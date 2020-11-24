y = 200 # global scope

def myfunc():
    x = 300 #local scope
    print(y)
    def myinnerfunc():
        print(x) # function inside function
    myinnerfunc()

myfunc()
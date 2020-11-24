class MyClass: # create class
    x = 5
p1 = MyClass() # create object
print(p1.x)

# __init__() function

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print('Hello my name is ' + self.name)

zul = person('zul',19)
zul.myfunc()

# The self parameter
class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print('hello my name is ' + abc.name)

p1 = Person('John', 36)
p1.myfunc()
p1.name = 'suep' # modify Object Properties
p1.myfunc()

class mahasiswa:

    __nilai = 0

    def __init__(self, name, nim):
        self.name = name
        self.nim = nim

    def uts(self, input_nilai):
        self.__nilai += input_nilai

    def uas(self, input_nilai):
        self.__nilai += input_nilai

    def check_status(self):
        if self.__nilai > 80:
            print(self.name, 'anda lulus')
        else:
            print(self.name, 'anda tidak lulus')

p1 = mahasiswa('zul', 1803)
p1.uts(30)
p1.uas(60)
p1.check_status()
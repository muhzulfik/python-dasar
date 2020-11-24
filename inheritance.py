class mahasiswa:
    def __init__(self, name, nim):
        self.name = name
        self.nim = nim

    def printname(self):
        print(self.name , self.nim)

x = mahasiswa('zul', 1803000)
x.printname()

class student(mahasiswa):
    def __init__(self, name, nim, prodi):
        super().__init__(name, nim)
        self.prodi = prodi # add methods
y = student('suep', 1803, 'informatika')
print(y.prodi)
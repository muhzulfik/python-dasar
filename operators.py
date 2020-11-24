x = int(input("Masukkan angka: "))
y = int(input("Masukkan angka: "))

# Arithmetic Operator
print(x + y)
print(x - y)
print(x / y)
print(x % y)
print(x * y)
print(x // y)
print(x ** y)

print(50*"=")

print("\"Comparism Operator\"")
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

print(50*"=")

print("\"Python Logical Operators\"")
print(x > 5 and y > 5)
print(x > 5 or y > 5)
print(not(x > 5 and y > 5))

print(50*"=")

print("\"Python Identity Operators\"")
print(x is y)
print(x is not y)

print(50*"=")

x = ['banana', 'grape']
y = ['banana', 'grape']

print("\"Python Membership Operators\"")
print(x in y)
print(x not in y)
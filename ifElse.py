a = int(input("Masukkan Angka: "))
b = int(input("Masukkan Angka: "))


if b > a: # If
    print('b greater than a')
elif a == b: # elif
    print('a and b are equal')
else: # else
    print('a is greater than b')


c = int(input("Masukkan Angka: "))

# AND
if a > b and c > a:
    print("Both conditions are True")

# OR
if a > b or a > c:
    print('At least one of the conditions is True')

# Nested If
x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print('and also above 20!')
    else:
        print('but not above 20.')
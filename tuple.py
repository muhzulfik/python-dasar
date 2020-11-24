fruits = ('apple', 'pinapple', 'mango')
print(fruits)
print(type(fruits))
print(fruits.count('apple'))

print(fruits[1])
print(fruits[-1])
print(fruits[0:2])
print(fruits[-3:-1])
print(len(fruits))

y = list(fruits)
print(y)
print(type(y))
y[1] = 'tomatto'
print(y)
fruits = tuple(y)
print(fruits)

for i in fruits:
    print(i)
    if i == 'mango':
        txt = "{} ditemukan"
        print(txt.format(i))
fruits = ['banana', 'grape', 'mango', 'startfruit']
print(fruits)

# access Items
print(fruits[2]) # 2 is mango

# negative indexing
# negative indexing start from 0
print(fruits[-1]) # -1 is startfruit

# range of indexes
print(fruits[1:3]) # 1 until 3 is grape, mango
print(fruits[:3])
print(fruits[1:])

# range of negative indexes
print(fruits[-3:-1])

# change item value
fruits[0] = 'papaya'
print(fruits)

print(50*('='))
# Loop Through a List
food = ['nasi goreng', 'ketoprak', 'ayam bakar']
for i in food:
    print(i)
    if 'nasi goreng' in i:
        print('Yes, nasi goreng is in food list')

# list length
print(len(food))

# Add items
food.append('kerak telur')
print(food)

food.insert(1, 'gorengan')
print(food)

# remove item
food.remove('ketoprak')
print(food)

food.pop()
print(food)

del food[0]
print(food)

food.clear()
print(food)

drink = ['chatime', 'bubble tea', 'frutang']
txt = 'i like drink {}'
print(txt.format(drink[0]))
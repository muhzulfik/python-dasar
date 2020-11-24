fruits = ['apple', 'grape', 'mango']
for x in fruits:
    print(x)

# Looping Through a string
for x in 'banana':
    print(x)

# Break
for x in fruits:
    print(x)
    if x == 'grape':
        break

# Continue Statement
food = ['rendang', 'sushi', 'kwetiau']
for x in food:
    if x == 'sushi':
        continue
    print(x)

# range function
for x in range(0, 10, 2):
    print(x)

# Else in for loop
for x in range(6):
    print(x)
else:
    print('Finally Finished')

# Nested For loop
color = ['red', 'yellow', 'purple']
fruits = ['apple', 'banana', 'grape']

for x in color:
    for y in fruits:
        print(x,y)

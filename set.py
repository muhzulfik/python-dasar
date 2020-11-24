fruits = {'banana', 'grape', 'pinapple'}
print(type(fruits))
print(fruits)

# Access Items
for x in fruits:
    print(x)

# Add Items
fruits.add('apple')
print(fruits)
fruits.update(['sawo','rasberry'])
print(fruits)

# Get The Length
print(len(fruits))

# Remove Item
fruits.remove("banana")
print(fruits)
fruits.discard("banana")
print(fruits)
fruits.pop()
print(fruits)
fruits.clear() #empties the set
print(fruits)
del fruits # delete the set

# Join Two Set
fruits1 = {'banana', 'grape', 'pinapple'}
fruits2 = {'apple', 'mango', 'jackfruits'}
fruits4 = {'sawo'}

fruits3 = fruits1.union(fruits2)
print(fruits3)

fruits1.update(fruits2)
print(fruits1)



thisdict = {
    'brand': 'toyota',
    'model': 'avanza',
    'year': 2011
}
print(thisdict)

#Access Item
print(thisdict['brand'])
print(thisdict.get('model'))

#Change Values
thisdict['year'] = 2019
print(thisdict)

# Loop through a dictionary

# this loop return value keys
for x in thisdict:
    print(x)

# this loop return the value
for x in thisdict:
    print(thisdict[x])

for x in thisdict.values():
    print(x)

for x, y in thisdict.items():
    print(x,y)

# check if key exist
thisdict = {
    'brand': 'toyota',
    'model': 'avanza',
    'year': 2011
}

if "model" in thisdict:
    print("yes, 'model' is one of the keys")

# dictionary length
print(len(thisdict))

# Removing Items
thisdict.pop('model')
print(thisdict)

thisdict.popitem()
print(thisdict)

del thisdict['brand'] # del same as pop
print(thisdict)

thisdict.clear() # empty the dictionary
print(thisdict)

del thisdict

# Copy a dictionary
thisdict = {
    'brand': 'toyota',
    'model': 'avanza',
    'year': 2011
}

mydict = thisdict.copy()
print(mydict)

anotherdict = dict(thisdict)
print(anotherdict)

# Nested Dictionary

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)
myfamily.popitem()
print(myfamily)

for x,y in myfamily.items():
    print(x,y)
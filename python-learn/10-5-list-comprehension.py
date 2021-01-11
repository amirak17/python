

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
print('\n----\n')

# one liner
newlist = [x for x in fruits if "a" in x]
print(newlist)

# -------

# Only accept items that are not "apple":
newlist = [x for x in fruits if x != "apple"]
print(newlist)
print('\n----\n')

# With no if statement:
newlist = [x for x in fruits]
print(newlist)
print('\n----\n')

# range
newlist = [x for x in range(10)]
print(newlist)
print('\n----\n')

# Accept only numbers lower than 5:
newlist = [x for x in range(10) if x < 5]
print(newlist)
print('\n----\n')

# Set the values in the new list to upper case:
newlist = [x.upper() for x in fruits]
print(newlist)
print('\n----\n')

# Set all values in the new list to 'hello':
newlist = ['hello' for x in fruits]
print(newlist)
print('\n----\n')

# Return "orange" instead of "banana":
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
print('\n----\n')

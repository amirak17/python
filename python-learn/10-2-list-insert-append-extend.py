
print('insert')
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
print('\n----\n')

print('append')
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
print('\n----\n')

print('extend')
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
print('\n----\n')

print('extend - tuple into list')
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
print('\n----\n')

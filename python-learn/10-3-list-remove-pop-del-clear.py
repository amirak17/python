
print('remove')
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
print('\n----\n')

print('pop')
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
print('\n----\n')

print('pop specific')
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
print('\n----\n')

print('del')
thislist = ["apple", "banana", "cherry"]
del thislist
print('\n----\n')

print('del specific')
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
print('\n----\n')

print('clear')
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
print('\n----\n')

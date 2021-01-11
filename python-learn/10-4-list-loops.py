# Loop Through a List
# https://www.w3schools.com/python/python_lists_loop.asp

# for
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
print('\n----\n')

# for - range - len
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
print('\n----\n')

# while - len
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
print('\n----\n')

# print for
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

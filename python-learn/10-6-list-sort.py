
# sort
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
print('\n------\n')

# sort numbers
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
print('\n------\n')

# reverse sort
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
print('\n------\n')

# reverse sort numbers
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
print('\n------\n')

# customize sort function
# The function will return a number that will be used to sort the list (the lowest number first):
# Sort the list based on how close the number is to 50:

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
print('\n------\n')

# case insensitive sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
print('\n------\n')

# perform a case-insensitive sort of the list:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
print('\n------\n')

# .reverse
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
print('\n------\n')

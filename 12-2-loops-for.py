"""
python for loops
a for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
"""

print('for loop list')
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

print('\n----\n')

print('looping through a string')
for x in "banana":
  print(x)

print('\n----\n')

print('the break statement')
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

print('\n----\n')

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)


print('the continue statement - do not print banana')
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

print('\n----\n')

print('the range() function')
for x in range(6):
  print(x)

print('\n----\n')

print('using the start parameter')
for x in range(2, 6):
  print(x)

print('\n----\n')

print('range increment the sequence with 3 (default is 1)')
for x in range(2, 30, 3):
  print(x)

print('else in for loop')
# note: the else block will not be executed if the loop is stopped by a break statement.
for x in range(6):
  print(x)
else:
  print("finally finished!")

print('\n----\n')

print('break the loop when x is 3, and see what happens with the else block')
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("finally finished!")

print('\n----\n')

print('nested loops')
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

print('\n----\n')

print('the pass statement')
for x in [0, 1, 2]:
  pass

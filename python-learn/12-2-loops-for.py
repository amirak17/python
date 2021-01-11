"""
python for loops
a for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
"""

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

print('\n----\n')

# looping through a string
for x in "banana":
  print(x)

print('\n----\n')

# the break statement
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

# the continue statement
# do not print banana:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

print('\n----\n')

# the range() function
for x in range(6):
  print(x)

print('\n----\n')

# using the start parameter:
for x in range(2, 6):
  print(x)

print('\n----\n')

# range increment the sequence with 3 (default is 1):
for x in range(2, 30, 3):
  print(x)

# else in for loop
# note: the else block will not be executed if the loop is stopped by a break statement.
for x in range(6):
  print(x)
else:
  print("finally finished!")

print('\n----\n')

# break the loop when x is 3, and see what happens with the else block:
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("finally finished!")

print('\n----\n')

# nested loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

print('\n----\n')

# the pass statement
for x in [0, 1, 2]:
  pass

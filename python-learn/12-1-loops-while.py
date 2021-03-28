"""
python loops
python has two primitive loop commands:

while loops
for loops
"""
# the while loop
print('print i as long as i is less than 6')
i = 1
while i < 6:
  print(i)
  i += 1

print('\n----\n')

print('the break statement')
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

print('\n----\n')

print('the continue statement')
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

print('\n----\n')

print('the else statement')
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

print('\n----\n')

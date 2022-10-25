
print('format:')
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
print('\n----\n')

print('format multiple vars into str')
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
print('\n----\n')

print('format multiple vars into str with placement of vars')
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

age = 36
# txt = "My name is John, I am " + age ----> will give error
print(txt)

print('escape string')
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

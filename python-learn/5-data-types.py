
# text type:	    str
# numeric types:	int, float, complex
# sequence types:	list, tuple, range
# mapping type:	    dict
# set types:	    set, frozenset
# boolean type:	    bool
# binary types:	    bytes, bytearray, memoryview



print('\n----\n')
print('data types')
x = "hello world"	# str
x = 20	    # int
x = 20.5	# float
x = 1j	    # complex

x = True	# bool
print('boolean:')
print(x)

print('\n----\n')

x = b"hello"	# bytes
print('bytes:')
print(x)

print('\n----\n')

x = bytearray(5)	# bytearray
print('bytearray:')
print(x)

print('\n----\n')

x = memoryview(bytes(5))	# memoryview
print('memoryview:')
print(x)

print('\n----\n')
print('\n----\n')

print('list:')
x = ["list", "apple", "banana", "cherry"]	# list: ordered and changeable, allows duplicate members
for i in x:
  print(i)
print('\n----\n')

print('tuple:')
x = ("tuple", "apple", "banana", "cherry")	# tuple: ordered and unchangeable, allows duplicate members.
for i in x:
  print(i)
print('\n----\n')

print('dict:')
x = {"type": "dict", "name" : "john", "age" : 36}	# dict: unordered and changeable, no duplicate members
print(type(x))
print(len(x))
for i, j in x.items():
  print(i, j)
print('\n----\n')

print('set:')
x = {"set", "apple", "banana", "cherry"}	# set: unordered and unindexed, no duplicate members.
for i in x:
  print(i)
print('\n----\n')

print('frozenset:')
x = frozenset({"frozen set", "apple", "banana", "cherry"})
for i in x:
  print(i)
print('\n----\n')

print('range:')
x = range(6)
for i in x:
  print(i)
print('\n----\n')

print('float:')
x = 35e3
y = 12e4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z))
print('\n----\n')

print('complex:')
x = 3+5j
y = 5j
z = -5j
print(x)
print(type(x))
print(y)
print(type(y))
print(z)
print(type(z))
print('\n----\n')

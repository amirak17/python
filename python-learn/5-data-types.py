
# Text Type:	    str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	    dict
# Set Types:	    set, frozenset
# Boolean Type:	    bool
# Binary Types:	    bytes, bytearray, memoryview



print('----')
x = "Hello World"	# str
x = 20	# int
x = 20.5	# float
x = 1j	# complex

x = True	# bool
x = b"Hello"	# bytes
x = bytearray(5)	# bytearray
x = memoryview(bytes(5))	# memoryview


x = ["LIST", "apple", "banana", "cherry"]	# list: ordered and changeable, allows duplicate members
for i in x:
  print(i)
print('----')

x = ("TUPLE", "apple", "banana", "cherry")	# tuple: ordered and unchangeable, allows duplicate members.
for i in x:
  print(i)
print('----')

x = {"Type": "DICT", "name" : "John", "age" : 36}	# dict: unordered and changeable, no duplicate members
print(type(x))
print(len(x))
for i, j in x.items():
  print(i, j)
print('----')

x = {"SET", "apple", "banana", "cherry"}	# set: unordered and unindexed, no duplicate members.
for i in x:
  print(i)
print('----')

x = frozenset({"FROZEN SET", "apple", "banana", "cherry"})	# frozenset
for i in x:
  print(i)
print('----')

x = range(6)	# range
for i in x:
  print(i)
print('----')

# floats
x = 35e3
y = 12E4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z))
print('----')

# complex
x = 3+5j
y = 5j
z = -5j
print(x)
print(type(x))
print(y)
print(type(y))
print(z)
print(type(z))
print('----')

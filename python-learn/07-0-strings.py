
print("hello")
print('hello')
print('\n----\n')

a = "hello"
print(a)
print('\n----\n')

print('multiline strings double quotes')
a = """lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
print('\n----\n')

print('multiline strings single quotes')
a = '''lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
print('\n----\n')

print('first char of string')
a = "hello, world!"
print(a[1])
print('\n----\n')


print('loop through the letters in the str "banana"'):
for x in "banana":
  print(x)
print('\n----\n')

print('length for str')
a = "hello, world!"
print(len(a))
print('\n----\n')

print('check if "free" is present in the following text')
txt = "the best things in life are free!"
print("free" in txt)
print('\n----\n')

print('use it in an if statement')
txt = "the best things in life are free!"
if "free" in txt:
  print("yes, 'free' is present.")
print('\n----\n')

print('check if not')
txt = "the best things in life are free!"
print("expensive" not in txt)
print('\n----\n')

print('use it in an if statement')
txt = "the best things in life are free!"
if "expensive" not in txt:
  print("yes, 'expensive' is not present.")

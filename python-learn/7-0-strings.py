
print("Hello")
print('Hello')
print('\n----\n')

a = "Hello"
print(a)
print('\n----\n')

# Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
print('\n----\n')

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
print('\n----\n')

a = "Hello, World!"
print(a[1])
print('\n----\n')


# Loop through the letters in the word "banana":
for x in "banana":
  print(x)
print('\n----\n')

# Length
a = "Hello, World!"
print(len(a))
print('\n----\n')

# Check if "free" is present in the following text:
txt = "The best things in life are free!"
print("free" in txt)
print('\n----\n')

# Use it in an if statement:
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
print('\n----\n')

# Check if NOT
txt = "The best things in life are free!"
print("expensive" not in txt)
print('\n----\n')

# Use it in an if statement:
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("Yes, 'expensive' is NOT present.")

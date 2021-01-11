
# https://www.w3schools.com/python/python_strings_methods.asp

print('\n------\n')

# capitalize
print('capitalize:')
txt = "hello, and welcome to my world."
x = txt.capitalize()
print(x)
print('\n------\n')

# casefold
print('casefold:')
txt = "Hello, and Welcome to my world."
x = txt.casefold()
print(x)
print('\n------\n')

# center
print('center:')
txt = "banana"
x = txt.center(20)
print(x)
print('\n------\n')

# count
print('count:')
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)
print('\n------\n')

# encode
print('encode:')
txt = "My name is Ståle"
x = txt.encode()
print(x)
print('\n------\n')

# endswith
print('endswith:')
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)
print('\n------\n')

# expandtabs
print('expandtabs:')
txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
print(x)
print('\n------\n')

# find
txt = "Hello, welcome to my world."
x = txt.find("welcome") # 7
print(x)
print('\n------\n')

# format
# https://www.w3schools.com/python/ref_string_format.asp
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))
print('\n------\n')

# index
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)
print('\n------\n')

# isalnum
txt = "Company12"
x = txt.isalnum()
print(x)
print('\n------\n')

# isalpha
txt = "CompanyX"
x = txt.isalpha()
print(x)
print('\n------\n')

# isdecimal
txt = "\u0033" #unicode for 3
x = txt.isdecimal()
print(x)
print('\n------\n')

# isdigit
txt = "50800"
x = txt.isdigit()
print(x)
print('\n------\n')

# isidentifier
txt = "Demo"
x = txt.isidentifier()
print(x)
print('\n------\n')

# islower
txt = "hello world!"
x = txt.islower()
print(x)
print('\n------\n')

# isnumeric
txt = "565543"
x = txt.isnumeric()
print(x)
print('\n------\n')

# isprintable
txt = "Hello! Are you #1?"
x = txt.isprintable()
print(x)
print('\n------\n')

# isspace
txt = "   "
# txt = " A "
x = txt.isspace()
print(x)
print('\n------\n')

# istitle
txt = "Hello, And Welcome To My World!"
# txt = "hello, and welcome to my world!"
x = txt.istitle()
print(x)
print('\n------\n')

# isupper
txt = "THIS IS NOW!"
# txt = "tHIS IS NOW!"
x = txt.isupper()
print(x)
print('\n------\n')

# join
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)
print('\n------\n')

# ljust
txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")
print('\n------\n')

# lower
txt = "Hello my FRIENDS"
x = txt.lower()
print(x)
print('\n------\n')

# lstrip
txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")
print('\n------\n')

# maketrans
txt = "Hello Sam!";
mytable = txt.maketrans("S", "P");
print(txt.translate(mytable));
print('\n------\n')

# partition
txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)
print(type(x))
print('\n------\n')

# replace
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)
print('\n------\n')

# rfind - last occurrence of the string
txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(x)
print('\n------\n')

# rindex - last occurrence of the string - search between position 5 and 10
txt = "Hello, welcome to my world."
x = txt.rindex("e")
print(x)
# ---
x = txt.rindex("e", 5, 10)
print(x)
# ---
# If the value is not found, the rfind() method returns -1, but the rindex() method will raise an exception:
txt = "Hello, welcome to my world."
print(txt.rfind("q"))
# print(txt.rindex("q"))
print('\n------\n')

# rjust
txt = "banana"
x = txt.rjust(20)
print(x, "is my favorite fruit.")
print('\n------\n')

# rpartition
txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x)
print(type(x))
print('\n------\n')

# rsplit
txt = "apple, banana, cherry"
x = txt.rsplit(", ")
print(x)
print(type(x))
print('\n------\n')

# rstrip
txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")
print('\n------\n')

# split
txt = "welcome to the jungle"
x = txt.split()
print(x)
print(type(x))
print('\n------\n')

# splitlines
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x)
print(type(x))
print('\n------\n')

# startswith
txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)
print('\n------\n')

# strip
txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")
print('\n------\n')

# swapcase
txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x)
print('\n------\n')

# title
txt = "Welcome to my world"
x = txt.title()
print(x)
print('\n------\n')

# translate
#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80};
txt = "Hello Sam!";
print(txt.translate(mydict));
print('\n------\n')

# upper
txt = "Hello my friends"
x = txt.upper()
print(x)
print('\n------\n')

# zfill - zero fill
txt = "50"
x = txt.zfill(10)
print(x)
print('\n------\n')


# https://www.w3schools.com/python/python_strings_methods.asp

def prline():
    print('\n------\n')

prline()

# capitalize
print('capitalize:')
txt = "hello, and welcome to my world."
x = txt.capitalize()
print(x)
prline()

# casefold
print('casefold:')
txt = "Hello, and Welcome to my world."
x = txt.casefold()
print(x)
prline()

# center
print('center:')
txt = "banana"
x = txt.center(20)
print(x)
prline()

# count
print('count:')
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)
prline()

# encode
print('encode:')
txt = "My name is Ståle"
x = txt.encode()
print(x)
prline()

# endswith
print('endswith:')
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)
prline()

# expandtabs
print('expandtabs:')
txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
print(x)
prline()

# find
txt = "Hello, welcome to my world."
x = txt.find("welcome") # 7
print(x)
prline()

# format
# https://www.w3schools.com/python/ref_string_format.asp
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))
prline()

# index
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)
prline()

# isalnum
txt = "Company12"
x = txt.isalnum()
print(x)
prline()

# isalpha
txt = "CompanyX"
x = txt.isalpha()
print(x)
prline()

# isdecimal
txt = "\u0033" #unicode for 3
x = txt.isdecimal()
print(x)
prline()

# isdigit
txt = "50800"
x = txt.isdigit()
print(x)
prline()

# isidentifier
txt = "Demo"
x = txt.isidentifier()
print(x)
prline()

# islower
txt = "hello world!"
x = txt.islower()
print(x)
prline()

# isnumeric
txt = "565543"
x = txt.isnumeric()
print(x)
prline()

# isprintable
txt = "Hello! Are you #1?"
x = txt.isprintable()
print(x)
prline()

# isspace
txt = "   "
# txt = " A "
x = txt.isspace()
print(x)
prline()

# istitle
txt = "Hello, And Welcome To My World!"
# txt = "hello, and welcome to my world!"
x = txt.istitle()
print(x)
prline()

# isupper
txt = "THIS IS NOW!"
# txt = "tHIS IS NOW!"
x = txt.isupper()
print(x)
prline()

# join
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)
prline()

# ljust
txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")
prline()

# lower
txt = "Hello my FRIENDS"
x = txt.lower()
print(x)
prline()

# lstrip
txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")
prline()

# maketrans
txt = "Hello Sam!";
mytable = txt.maketrans("S", "P");
print(txt.translate(mytable));
prline()

# partition
txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)
print(type(x))
prline()

# replace
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)
prline()

# rfind - last occurrence of the string
txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(x)
prline()

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
prline()

# rjust
txt = "banana"
x = txt.rjust(20)
print(x, "is my favorite fruit.")
prline()

# rpartition
txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x)
print(type(x))
prline()

# rsplit
txt = "apple, banana, cherry"
x = txt.rsplit(", ")
print(x)
print(type(x))
prline()

# rstrip
txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")
prline()

# split
txt = "welcome to the jungle"
x = txt.split()
print(x)
print(type(x))
prline()

# splitlines
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x)
print(type(x))
prline()

# startswith
txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)
prline()

# strip
txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")
prline()

# swapcase
txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x)
prline()

# title
txt = "Welcome to my world"
x = txt.title()
print(x)
prline()

# translate
#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80};
txt = "Hello Sam!";
print(txt.translate(mydict));
prline()

# upper
txt = "Hello my friends"
x = txt.upper()
print(x)
prline()

# zfill - zero fill
txt = "50"
x = txt.zfill(10)
print(x)
prline()

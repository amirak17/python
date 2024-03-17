
import json

print('JSON')
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)
print(y["age"])

print('\n----\n')




print('Convert from Python to JSON')
# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.
import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

y = json.dumps(x) # convert into JSON:
print(y)

print('\n----\n')



print('Convert from Python objects to JSON')
# You can convert Python objects of the following types, into JSON strings:
# dict, list, tuple, string, int, float, True, False, None

import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

print('\n----\n')






print('Convert JSON')

# When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:
#
# Python	 JSON
# dict	     Object
# list	     Array
# tuple	     Array
# str	     String
# int	     Number
# float	     Number
# True	     true
# False	     false
# None	     null

# Convert a Python object containing all the legal data types:

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

y = json.dumps(x)

print(type(x)) # dict
print(type(y)) # str
print(json.dumps(x))

print('\n----\n')





print('Format the Result - using indent')
# The example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks.
# The json.dumps() method has parameters to make it easier to read the result:

# Use the indent parameter to define the numbers of indents:

print(json.dumps(x, indent=4))

print('\n----\n')



print('Format the Result - using indent, separators')
# You can also define the separators, default value is (", ", ": "),
# which means using a comma and a space to separate each object, and a colon and a space to separate keys from values:
# Use the separators parameter to change the default separator:
print(json.dumps(x, indent=4, separators=(". ", " = ")))

print('\n----\n')



print('Order the Result')
# The json.dumps() method has parameters to order the keys in the result:
# Use the sort_keys parameter to specify if the result should be sorted or not:
print(type(json.dumps(x, indent=4, sort_keys=True)))
print(json.dumps(x, indent=4, sort_keys=True))

print('\n----\n')






import requests 
import sys 

if len(sys.argv) != 2:
    sys.exit() 

# https://itunes.apple.com/search?entity=song&limit=1&term=weezer

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(response.json())
print(json.dumps(response.json()))

o = response.json() 
for result in o["results"] : 
    print (result["trackName"])

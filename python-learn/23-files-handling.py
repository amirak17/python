"""
Python File Open
File handling is an important part of any web application.

Python has several functions for creating, reading, updating, and deleting files.

File Handling
The key function for working with files in Python is the open() function.

The open() function takes two parameters; filename, and mode.

There are four different methods (modes) for opening a file:

"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)

Syntax
To open a file for reading it is enough to specify the name of the file:

f = open("demofile.txt")
The code above is the same as:

f = open("demofile.txt", "rt")
Because "r" for read, and "t" for text are the default values, you do not need to specify them.

Note: Make sure the file exists, or else you will get an error.
"""







print('READ FILES')
# Open a File on the Server
# Assume we have the following file, located in the same folder as Python:
# demofile.txt
# Hello! Welcome to demofile.txt

# The open() function returns a file object, which has a read() method for reading the content of the file:

f = open("demofile.txt", "r")
print(f.read())
# If the file is located in a different location, you will have to specify the file path

# Read Only Parts of the File
# By default the read() method returns the whole text, but you can also specify how many characters you want to return:
# Return the 5 first characters of the file:

f = open("demofile.txt", "r")
print(f.read(5))

print('\n----\n')




print('Read Lines using readline()')
# You can return one line by using the readline() method:
f = open("demofile.txt", "r")
print(f.readline())
print('\n----\n')




print('Mutiple readline()')
# By calling readline() two times, you can read the two first lines:
f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())
print('\n----\n')




print('Loop')
# By looping through the lines of the file, you can read the whole file, line by line:
f = open("demofile.txt", "r")
for x in f:
  print(x)
print('\n----\n')



print('Close Files')
# It is a good practice to always close the file when you are done with it.
f = open("demofile.txt", "r")
print(f.readline())
f.close()
# Note: You should always close your files,
# in some cases, due to buffering, changes made to a file may not show until you close the file.






print('File Write')
# Write to an Existing File

# To write to an existing file, you must add a parameter to the open() function:
# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content

f = open("demofile.txt", "a")
f.write("Now the file has more content!\n")
f.close()

# Open and read the file after the appending:
f = open("demofile.txt", "r")
print(f.read())
# Example

# Open the file "demofile3.txt" and overwrite the content:
#
# f = open("demofile3.txt", "w")
# f.write("Woops! I have deleted the content!")
# f.close()
#
# #open and read the file after the appending:
# f = open("demofile3.txt", "r")
# print(f.read())
# Note: the "w" method will overwrite the entire file.
#
# Create a New File
# To create a new file in Python, use the open() method, with one of the following parameters:
#
# "x" - Create - will create a file, returns an error if the file exist
# "a" - Append - will create a file if the specified file does not exist
# "w" - Write - will create a file if the specified file does not exist
#
# Example
# Create a file called "myfile.txt":
#
# f = open("myfile.txt", "x")
# Result: a new empty file is created!
#
# Example
# Create a new file if it does not exist:
#
# f = open("myfile.txt", "w")







print('Delete a File')
# To delete a file, you must import the OS module, and run its os.remove() function:

# Check if File exist:
# To avoid getting an error, you might want to check if the file exists before you try to delete it:

import os
if os.path.exists("demofile.txt"):
  os.remove("abc.txt")
else:
  print("The file does not exist")


print('Delete Folder')
import os
os.rmdir("myfolder")
# Note: You can only remove empty folders.

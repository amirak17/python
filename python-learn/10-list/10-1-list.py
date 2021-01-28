# https://www.w3schools.com/python/python_lists.asp
"""
Python Collections (Arrays)

There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered and unindexed. No duplicate members.
Dictionary is a collection which is unordered and changeable. No duplicate members.

List Methods

Python has a set of built-in methods that you can use on lists.

append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count() 	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list
"""

print('show list')
thislist = ["apple", "banana", "cherry"]
print(thislist)
print('\n----\n')

print('access a member')
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
print('\n----\n')

print('change a member eg, 1')
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
print('\n----\n')

print('change a member eg, 2')
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
print('\n----\n')

print('change a member eg, 3')
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
print('\n----\n')

print('change a member eg, 4')
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
print('\n----\n')

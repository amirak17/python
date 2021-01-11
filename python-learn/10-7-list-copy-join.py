
# copy list 1
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
print('\n------\n')

# copy list 2
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
print('\n------\n')




# join

# with +
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
print('\n------\n')


# append
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
print('\n------\n')


# extend
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
print('\n------\n')

# Lists are ordered sequences that can hold variety of object types
# use [] and comma to seperate objects [1,2,3,4,5]
# Lists supports indexing and slicing
# List of integers
my_list = [1,2,3,4,5]
print(my_list)
#List of different object types
my_list = ['Sanjay',12,'fox', 12.54]
print(my_list)

#Check the length of the list
print(len(my_list))

#List is same as String as far indexing and Slicing is concern
print(my_list[0]) # grab first object

print(my_list[1:])

#Concatenate two lists
another_list = ['qa','team']

print(my_list + another_list)

#String is immutable but list can be manipulated
new_list = ['one','two','three']
print(new_list)
#let's replace first object
new_list[0] = 'ONE IN UPPER'
print(new_list)

# appending a object to list
new_list.append('four')
print(new_list)

# Lets remove one object from list
new_list.pop() # four will be removed from the list
print(new_list)

# removing an item by its index
new_list.pop(0)
print(new_list)

# Sorting a list
next_list = ['a', 'g', 'd', 'c','b']
num_list = [2,6,23,12,11]

next_list.sort()
print(next_list)

num_list.sort()
print(num_list)

# Let's reverse everything in the list
next_list.reverse()
print(next_list)

num_list.reverse()
print(num_list)
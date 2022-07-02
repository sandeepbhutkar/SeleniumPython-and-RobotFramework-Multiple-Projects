# Many objects in python are iterable, meaning we can iterate over every element in the object
# we can use For loops to execute a block of code for every iteration
mylist = [1,2,3,4,5,6,7]
for num in mylist:
    print(num)
# num in above example is a placeholder it can be anything e.g. i, xyz

# lets find out even odd in above list
for num in mylist:
    if num % 2== 0:
        print(f"Number is even:{num}")
    else:
        print(f"Number is odd:{num}")

#Lets try to get sum of all the numbers present in mylist
listsum = 0
for num in mylist:
    listsum = listsum + num

print(f"sum of the list is: {listsum}")

#Lets take more example, this time use string
mystring = "Word is beautiful"
for letter in mystring:
    print(letter)

# Lets take one more example, this time use tuple
    mytup = (1,2,3,4,5,6)
    for tup in mytup:
        print(tup)

#Lets take list of tuples
mylistoftup = [(1,2),(3,4),(5,8),(7,4)]
print(len(mylistoftup))
for item in mylistoftup:
    print(item)
#now, we are going to see example of tuple unpacking
for a,b in mylistoftup:
    print(a)
    print(b)
# in above example (a,b) is a temporary variable in form of tuple

########Lets take dictionary
d = {'k1':1, 'k2':2,'k3':5}
for item in d:
    print(item) # it will print keys only

for item in d.items():
    print(item) # it will return key and value

for a,b in d.items():
    print(a)
    print(b) # we can use temporary variables to retrive key values
# we can use below technique if we want only values
for value in d.values():
    print(value)

# we can use below technique if we want only keys
for item in d.keys():
    print(item)
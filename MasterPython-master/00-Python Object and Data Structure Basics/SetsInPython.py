# Sets are unordered collection of unique objects
mySet = set()
mySet.add(1)
print(mySet)

mySet.add(2)
print(mySet)

#Lets try to add same value to the set
mySet.add(2)
print(mySet) # it does not add a duplicate element

myList = [1,3,2,4,5,2,2,4,1] # list having repeated elements
s = set(myList)
print(s) # removes all duplicate elements and creates set of unique elements
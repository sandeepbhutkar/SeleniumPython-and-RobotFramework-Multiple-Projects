# ex1 range operator (its kind of generator which generates numbers for you)
for num in range(10):
    print(num) # will display 0 to 9
#ex2
for num in range(2,8):
    print(num) # will display 2 to 7
#ex3
for num in range(2,8):
    print(num) # will display 2 to 7
#ex4
for num in range(2,8,2):
    print(num) # will display 2, 4 & 6 as we are using start, stop, step syntax
# ex5 lets you want to create a list
mylist = list(range(1,10,2))
print(mylist)
############## Example of Enumerate
index_count = 0
s = "World is Beautifull"
for letter in s:
    print("At index {} the letter is {}".format(index_count,letter))
    index_count += 1
# lets re-write same code with enumerate
for item in enumerate(s):
    print(item) # it returns tuple of index and letter
# As we already know how to unpack tupe lets do it here
for index,letter in enumerate(s):
     print(index)
     print(letter)
     print('\n')

###### ZIP is used to bring to list together and returns a tuple
mylist1 = [1,2,3]
mylist2 = ['a','b','c']
zippedList = list(zip(mylist1,mylist2))
print(zippedList)
####### IN key word can be used to check if item is present in list
print('b' in mylist2) # is b present in the list

print('f' in mylist2)# is f present in the list
## Another example
print('world' in 'The world is Beautifull!') # is 'world' present in given string
# it works same way in dictionary as well
dict = {'id':123,'name':'sanjay','age':35}
print('age' in dict.keys())
print('sanjay' in dict.values())

# MIN MAX functions
mylist3 = [10,34,24,56,76,9]
print(min(mylist3))
print(max(mylist3))

# Random libraray
from random import shuffle # lets import library first
l1 = [1,2,3,4,5,6,7,8,9,10]
shuffle(l1)
print(l1) # it shuffles the items in random order

###### How to accept user input#############
num = input("Enter a number here  ")
print(num) # input always treats input as string, that means number is also string. lets check
print(type(num)) # <class 'str'>
# you have to type cast the input data
num2 = int(num)
print(type(num2)) #<class 'int'>
# alternate way to acheive the same result is:
num3 = int(input("Enter a number here  "))
print(type(num3))




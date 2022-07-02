# map is in-built function in python which expects a function and iterable as an argument
# Lets create a simple function that squares a number
def square(num):
    return num**2
# we have a list of items and we have to aply map function on it, which will return square of each items
my_num = [1,2,3,4,5]

for item in map(square,my_num):
    print(item)
# or you can use as below to get a list
print(list(map(square,my_num)))

# Lets create a function that retruns even when length of string is even else returns first character of string

def splicer(mystring):
    if len(mystring) % 2 == 0:
        return "EVEN"
    else:
        return mystring[0]

names = ['Sanjay','MDP','Deepak','Sandeep','Rizwan','Nawaz','Aruna']

print(list(map(splicer,names)))
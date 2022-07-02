# filter(function or None, iterable) --> filter object
# Return an iterator yielding those items of iterable for which function(item)
# is true. If function is None, return the items that are true.

### Lets write a functio that checks number is even and returns True/False
def check_even(num):
    return num % 2 == 0

print(check_even(4))

mylist = [1,2,3,4,5,6,7,8,9,10]

print(list(filter(check_even, mylist))) # will return a list of even numbers
# we can use for loop also to get the numbers
for num in filter(check_even, mylist):
    print(num)
# Tuples are similar to Lists, However have only key difference - Immutability
# Once an element is inside tuple, it can not be reassigned
# Tuples uses Parenthesis (1,2,3,4)
t = (1,2,3,4,5)

myList = [1,2,3,4,5]

print(type(t)) # tuple

print(type(myList)) # list

# tuple can have different object types
t = ('sunny',2,5,12.5,'sunny')
print(t[0]) # Slicing as a list
print(t[-1])
# count method available with Tuple
print(t.count('sunny')) # how many times 'sunny' appears in tuple

t[0] = 'NEW'  # this line must give error as tuple is immutable



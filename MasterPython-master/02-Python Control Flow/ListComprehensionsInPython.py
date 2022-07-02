# List comprehensions are quickest way to create a list
# If you are using for loop and using .append() the this is good candidate of comprehension
# conventional way of doing it:
mystring = 'World is beautifull'
mylist = []
for item in mystring:
    mylist.append(item)
print(mylist)

# will apply list comprehension to above example
mylist = [item for item in mystring ]
print(mylist) # isn't it quicker way

# Lets take one more example to re-inforce it
s =[x for x in 'hello']
print(s)
# This is also called flattening of FOR Loop. take one more use case
l = [num**2 for num in range(1,10,2)]
print(l)
# lets put a check in above example . grab only square of even numbers
n = [num**2 for num in range(1,10) if num %2 == 0]
print(n)

# Lets try concept and convert temperature from Fahrenheite to Celcius
f = [32.0, 50.0, 68.0, 94.1]
celcius = [((temp - 32) * 5/9) for temp in f]
print(celcius)


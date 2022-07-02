# Strings are sequence of characters using single or double quotes like 'Hello' or "Hello"
# "I don't do that"
print('hello')
print("hello")
print("I don't do this")
# Characters:   h e l l o
# index:        0 1 2 3 4
# Reverse index:0 -4 -3 -2 -1
print('hello \n world')
print('hello \t world')

myString = 'hello'
print(len(myString))

#grab first character from string
print(myString[0])
# Slicing allows to grab a susection of multiple characters this has syntax [start:Stop:step]
# start is numeric index for the slice start
#get the value by reverse indexing, get 'l' from myString
print(myString[-2])

#Slicing, getting the string starting from a perticular character
# Say we want to grab all the characters after 'e'
print(myString[2:])

# say we want to grab first 3 characters (Upper bound is always excluded
print(myString[:3])

#garb characters 'ell' from string
print(myString[1:4])

# Lets reverse the string dabaredyH  using start, stop and step
place = 'Hyderabad'
print(place[::-1])
# Immutability of strings, means you can not change a string say 'Tanu' to 'Manu'
name = 'Tanu'
# name[0] = 'M'

# you will get an error "TypeError: 'str' object does not support item assignment"
# instead you have to use concatenation
last_letters = name[1:] # get last three letters from name
print(last_letters)
# lets concetenate 'M' to last_letters
new_name = 'M' + last_letters
print(new_name)

#String multiplication
letter = 'z'
print(letter * 10) # will give zzzzzzzzzz

# numerals as String
print('2' + '3') # it will concatenate instead of addition and you will get 23

#There are various String methods available, we will go through few
msg = 'Hello World'
# Change to upper case and lower case
print(msg.upper())

print(msg.lower())

#Splitting the string
print(msg.split()) # By default string will be splitted on space



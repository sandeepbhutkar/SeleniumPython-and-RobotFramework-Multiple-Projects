# injecting a variable in your string for printing
# It is also known as String interpolation
my_name = 'Sanjay'
print('Hello ' + my_name)

#let's explore two methods .format() and f-strings(formatted string laterals)
print("this is string {}".format("Inserted"))

#Let's insert string multiple places
print("Once {} a time  {} was a {}".format("upon","there","fox"))

# we can assign these strings to variable

print('Once {u} a time {w} was a {a}'.format(u ='upon',w ='there', a = 'fox'))

# If you want to print fox fox fox

print('Once {a} a time {a} was a {a}'.format(u ='upon',w ='there', a = 'fox'))

#Formatting a flot value using "{value:width.precision f}"
result = 22/7
print(result) #3.142857142857143
print("The value of Pi is: {r:1.3f}".format(r = result))

# using f-strings(formatted string laterals), this is available with Python 3.6
name = 'Sanjay'
print(f'Hello {name}') # Hello Sanjay

#One more example
name = 'Sanjay'
age = 35
gender = 'Male'

print(f'Meet {name}, he is {age} years old {gender}')
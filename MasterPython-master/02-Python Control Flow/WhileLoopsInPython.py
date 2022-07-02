# While loops will continue to execute a block of code while some condition remains True
# real time example...while corona infected count rate goes below 4 per day continue lockdown
# Syntax while some_boolean_condition:
# do something
# you can combine else also
# else:
# do something else
x = 0
while x < 5:
    print(f"current value of x is: {x}")
    x = x + 1
else:
    print(f"current value of : {x} is not less than 5")

##### Pass, break and continue keywords
mylist = [1,2,3]
for item in mylist:
    pass
print("I am working on this logic yet!!")
# when you are not quite sure what code block should be written in for loop you can use pass, this will "do nothing"

# Lets use 'continue' keyword
s = 'Beautifull'
for letter in s:
    if letter == 't':
        continue # suppose we dont want to print 't', when loop gets letter t it will redirects pointer to start of loop
    print(letter)

# lets use 'Break' in above example
for letter in s:
    if letter == 't':
        break # when loop gets letter t it will comes out of loop
    print(letter)

# StringIO module implements in-memory file like object, this object can be used as input or output to most functions
from io import StringIO

#Arbitrary string
message = 'This is  a just a normal string'

# Use StringIO method to set  as file object
f = StringIO(message)

print(f.read())

# we can write in to file
f.write("\nThis is the second line ")
# reset the cursor
f.seek(0)
# read the file again
print(f.read())

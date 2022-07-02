# named tuple assigns a name to element in tuple so that you can call it with name also
# it allows us to create a new object type that allows name for tuple elements
from collections import namedtuple
Dog = namedtuple('dog','age breed name')
sam = Dog(age=2,breed='Lab',name='sammy')
print(sam.age)
# we can also use index
print(sam[0])
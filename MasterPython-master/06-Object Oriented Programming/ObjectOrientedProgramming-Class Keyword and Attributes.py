# Lets define a very simple class using camel casing convention
class Sample():
    pass # will do nothing

#create an instance of the above SampleWord class
my_class = Sample()
print(type(my_class))

# lets take one example
class Dog():
    def __init__(self,breed,name,spots):  # init can be considered as constructor of class, self can be considered as instance of class
        self.breed = breed
        self.name = name
        # expecting boolean True/False for spots
        self.spots = spots
    #Attribute
    # We take in the argument
    # Assign it using self.Attribute_name


my_dog = Dog(breed='Lab',name='Sammy',spots=True)

print(type(my_dog))
print(my_dog.breed) # breed is an attribute
print(my_dog.name) # name is an attribute
print(my_dog.spots) # spots is an attribute
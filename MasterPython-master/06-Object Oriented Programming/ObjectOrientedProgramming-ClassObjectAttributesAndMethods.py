# lets take previous example
class Dog():
    # Lets define CLASS OBJECT Attribute
    # SAME FOR ANY INSTANCE OF CLASS
    species = 'mammal'

    #Below self init is used for user defined attribute
    def __init__(self,breed,name,spots):  # init can be considered as constructor of class, self can be considered as instance of class
        self.breed = breed
        self.name = name
        # expecting boolean True/False for spots
        self.spots = spots
    #Attribute
    # We take in the argument
    # Assign it using self.Attribute_name

    ######################Methods are function inside the class that performs operations that utilize attributes that we have created
    ## Operations/Action --->methods
    def bark(self,number):
        print("WOOF! woof! my name is  {} and my number is {}".format(self.name,number))


my_dog = Dog(breed='Lab',name='Sammy',spots=True)

print(type(my_dog))
print(my_dog.breed) # breed is an attribute
print(my_dog.name) # name is an attribute
print(my_dog.spots) # spots is an attribute
print(my_dog.species) # spots is an Class attribute
type(my_dog.bark(1)) # called method of class
##############################one more example####################################

class Circle():
    # lets create class Attribute
    pi = 3.14

    # User defined attributes
    def __init__(self,radius=1):
        self.radius = radius
        self.area = self.radius * self.radius * Circle.pi

    #Lets create a method
    def get_circumference(self):
        return 2* Circle.pi * self.radius

#Lets create an object of class
my_circle = Circle(10)

print(my_circle.pi)
print(my_circle.radius)
print(my_circle.area)

print(my_circle.get_circumference())


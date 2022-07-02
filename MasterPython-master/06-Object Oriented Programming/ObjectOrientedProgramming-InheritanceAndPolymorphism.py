## Inheritance is a way to define new classes using class that is already defined
## we can re-use code that is already defined and it reduces complexity of the program
# Lets create our base class
class Animal():
    def __init__(self):
        print("ANIMAL CREATED")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating!")
## Lets create a new class from base class that allow us to use methods of base class
class Dog(Animal): # Passing Animal...will inherit features from base class
    def __init__(self):
        Animal.__init__(self) #it will create an instance of Animal class when dog class is instance is created
        print("DOG CREATED")
# Lets overwrite eat() method of Animal class
    def who_am_i(self):
        print("I am a DOG")

    def eat(self):
        print("I am a dog, I am eating")
# lets add a new method in dog() class
    def bark(self):
        print("WOOF!")


mydog = Dog()
print(mydog.bark())
print(mydog)
#print(mydog.eat())

################## POLYMORPHISM ###################
## Two classes having same methods
class Horse():
    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + " says neighing!!"

class Cat():
    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + " says meow!!"

#lets call that class
chetak = Horse("chetak")
noori = Cat("noori")
print(chetak.speak())
print(noori.speak())

#for pet in [chetak,noori]:
#    print(pet.speak())

def pet_speak(pet):
    print(pet.speak())

pet_speak(chetak)

pet_speak(noori)
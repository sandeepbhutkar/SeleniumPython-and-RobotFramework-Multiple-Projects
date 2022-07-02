# Object Oriented Programming (OOP) allows programmers to create their own objects that have attributes and methos
#Like String, List, Dictionary objects have their own methods and we can call by .method_name() syntax
# these methods act as a function that use information about object
# In general, OOP allows us to create code taht is repeatable and organized
# Object definition synatx
class NameOfTheClass():
    def __init__(self,param1, param2):
        self.param1 = param1
        self.param2 = param2

    def some_method(self):
        #perform some action
        print(self.param1)
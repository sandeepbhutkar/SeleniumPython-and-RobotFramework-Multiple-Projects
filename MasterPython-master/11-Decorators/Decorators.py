# Decorators allow you to decorate a function
# Python has decorators that allow you to track on extra functionality to an existing function
# they use @ operator and are then placed on top of the original function
def hello():
    return "Hello!"
print(hello())

hello
greet = hello # assigning function to a variable

print(greet())
#Lets call hello()
print(hello())

# lets delete original hello()
del hello

# try to execute hello()
#print(hello()) #NameError: name 'hello' is not defined

# now check greet()
print(greet()) # greet still works
# that means greet still poiting to hello() object

# Lets create  one more function
def welcome(name='Sanjay'):
    print("the welcome() function has been executed!")

    def good_wish():
        return "\t this is good_wish() function inside the welcome() function"

    def warm_wish():
        return "\t this is warm_wish() function inside the welcome() function"

    #print(good_wish())
    #print(warm_wish())
    #print("This is the end of welcome() function!")
    print("I am going to return a function!")
    if name == 'Sanjay':
        return good_wish()
    else:
        return warm_wish()

# note that scope of good_wish() and warm_wish() functions are limited, you can not call directly these functions
# print(good_wish()) # NameError: name 'good_wish' is not defined
print(welcome())

# How to call these functions which are inside welcome() function

my_new_func = welcome('Sanjay')

print(my_new_func)

# Lets take on more example
def cool():

    def super_cool():
        return 'I am very cool!!'

    return super_cool()

# lets call above function

some_func = cool()

print(some_func)

######## Passing a function as an argument
def wishes():
    return 'Hi Sanjay!'

def other(some_def_func):
    print('other code runs here!!')
    print(some_def_func())

# let call other()
other(wishes)

################# Now we understand concept of passing function in a variable and as an argument, lets create
### decorators##########"

def new_decorator(original_func):

    def wrap_func():
        print("Some extra code, before the original function!")

        original_func()

        print("Some extra code, before the original function!")

    return  wrap_func()

def func_needs_decorator():
    print("I want to be decorated!")

decorated_func = new_decorator(func_needs_decorator)
print(decorated_func())

## same can be achieved using @ operator

@new_decorator
def func_needs_decorator():
    print("I want to be decorated!")
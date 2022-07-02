x = 25

def print_value():
    x = 50
    return x
# now, print(x) should return 25 or 50?
print(x) # it returns 25

print(print_value()) # returns 50

# How python knows which x assignment user is referring to?
# it because of Rule of Scope LEGB (local,Enclosing function, Global and Built-in)
# Example of Local
lambda num: num**2 # num is local to lambda

# example of Enclosing function
#GLOBAL
name = "This is global Name"

def greet():
    #ENCLOSING
    name = "I am enclosing"

    def hello():
        #LOCAL
        name= "I am local"
        print("Hello "+name)

    hello()

greet() # it returns Hello Sanjay because it finds name variable defined in enclosing function

############# Try re-running function after commenting name = "I am enclosing" step and check output

# Now, this time as neither local not enclosed function is g=having name variable it goes for Global
# we get "Hello This is global Name"
# Comment Local and execute  then comment enclosing and check scope

# Lets first write a function that returns 5% of sum


def myfunc(a, b, c=0, d=0):
    # Retunrs 5 % of sum of a & b
    return sum((a, b, c, d)) * 0.05


print(myfunc(30, 70))
print(myfunc(30, 70, 100))
print(myfunc(30, 70, 100, 200))


### lets use *args when no. arguments are not fixed, user can pass any number of arguments
def myfunct(*args):
    print(args)
    # Retunrs 5 % of sum of numbers
    # *args returns tuple
    return sum((args)) * 0.05


print(myfunct(30, 70))
print(myfunct(30, 70, 100))
print(myfunct(30, 70, 100, 200, 100, 34, 32, ))


#################### **kwargs always returns dictionary, kwargs means key word arguments

def myfun(**kwargs):
    print(kwargs)
    if 'fruit' in  kwargs:
        print("my favourite fruits is : {}".format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')


myfun(fruit = "apple",veggie = "Lettuce")

### using *args and **kwargs
def mysuper(*args,**kwargs):
    print(args)
    print(kwargs)
    print("I would like {} {}".format(args[0],kwargs['food']))


mysuper(1,13,14,veggie='lettuce',food='biryani', flower='tulip')
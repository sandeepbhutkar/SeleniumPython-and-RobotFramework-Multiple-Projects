# Generator functions allow us to write a function that can send back a value and then later resume to pick up
# where it left off. for example range() function does not create a list in memory for all the values from start to stop
# instead it just tracks last number and the step size, to provide flow of numbers

def create_cubes(n):
    for x in rage(n):
        yield x**3

create_cubes(10)

# lets take one more example
def gen_fibonacci(n):
    a = 1
    b = 1
    for x in range(n):
        yield a

        a,b = b, a+b

# lets use it
for number in gen_fibonacci(10):
    print(number)

# use iter() function, allows to iterate through a string
s = 'hello'
s = iter(s)
print(next(s))

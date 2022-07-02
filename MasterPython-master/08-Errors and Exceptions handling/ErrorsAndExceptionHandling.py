# Errors are bound to happen in your code, Especially someone else ends up using it in unexpected way
# We use error handling to attempt to plan for possible errors
# We can use error handling to let the script continue with other code, even if there is an error
# we can use three keywords
# try: this is the block of code to be attempted (may lead to an error)
# except: block of code will execute incase there is an error in try block
# finally: A final block of code to be executed, regardless of an error
# lets write a simple function to add two numbers
def add(n1,n2):
    sum = n1+n2
    return sum
# you decided to use above function and take n2 as an input from user

#n1 = 10
#n2 = input("please input a number..")
# now call above add function
#add(n1,n2)
#print("the sum of above two numbers is : ")

try:
    number1= 10
    number2 = int(input("please input a number.."))
    result = add(number1, number2)
    print(result)
# want to attempt this code, there could be an error
except:
    print("It seems you have entered incorrect data!!")
else:
    print("Hope you got sum of the two numbers")

### Lets try out another example with finally block
try:
    f = open('testfile','w')
    f.write("Write a test line to file")
except TypeError:
    print("There was a typeError !")
except OSError:
    print("You have an OS Error !")
finally:
    print("I always run no matter what!")

#### Lets try to write to file when opened in Read only mode
try:
    f = open('testfile','r')
    f.write("Write a test line to file")
except TypeError:
    print("There was a typeError !")
except OSError:
    print("You have an OS Error !")
finally:
    print("I always run no matter what!")

# lets try one more example to reinforce
def ask_for_int():
    try:
        result = int(input("Please provide number.."))
    except:
        print("Whoops!! this is not a number")
    finally:
        print("this is end of try/except/finally")

ask_for_int()

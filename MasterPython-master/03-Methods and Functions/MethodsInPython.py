# Built-in objects in Python have variety of methods that we can use
mylist = [1,2,3,4,5]
mylist.insert(5,6) # click on insert and hit cntrl + B to get the help
print(mylist)

# Functions allows us to create blocks of code that can be easily executed many times, without needing to
# constantly rewrite the entire block of code
def name_of_functions(name):
    ''' this is a simplest function '''
    print("Hello "+name)

name_of_functions('sanjay')

# one more simple function
def add_function(num1,num2):
    '''DOCSTRING: This is a simple function for addition
    INPUT: two numbers
    OUTPUT: Sum of two numbers'''
    return num1 + num2

result = add_function(2,3)
print(result)

# find out if string contains word 'dog' in it
def dog_check(mystring):
    return 'dog' in mystring.lower()

print(dog_check("where is my dog")) # returns boolean True or False

############## PIG LATIN Translator ###########################
# if word starts with vowel, add 'ay' at the end
# if word doesn't start with vowel, put first letter at the end and add 'ay'
# e.g word --> ordway
# e.g. apple --> appleay
def pig_latin(word):
    first_letter =  word[0]
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter[0] +'ay'
    return pig_word

print(pig_latin('asia'))
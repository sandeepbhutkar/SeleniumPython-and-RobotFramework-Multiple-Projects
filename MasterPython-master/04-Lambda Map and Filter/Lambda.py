# Lets try to covert a function in to Lambda function step-by-step
def square(num):
    result = num**2
    return result

print(square(4))

# step1 : lets get rid of a step in above function
def square(num):
    return num**2

print(square(3))

# step2: lets put code in one line
def square(num): return num**2

print(square(2))

# sometimes we used to write a function that is used one time and we don't want to give any name to this function
# Lets remove the function name and return
lambda num: num**2

print(square(5))

# lets try to use map and Lambda together
mynums = [1,2,3,4,5,6]
print(list(map(lambda num: num**2,mynums)))

# lets try to use filter and Lambda together
print(list(filter(lambda num:num%2 == 0,mynums)))

# lets try to grab first character from names list
mdp = ['Nawaz','Rizwan','Deepak','Tanu','Aruna','Laxmi','Sandeep','Divyarani','Vaishali']
print(list(map(lambda names:names[0],mdp)))
# Lets reverse our names
print(list(map(lambda names:names[::-1],mdp)))
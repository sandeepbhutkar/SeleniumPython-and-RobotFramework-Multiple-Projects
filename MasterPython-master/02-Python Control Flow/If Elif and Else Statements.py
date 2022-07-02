# We want to run certain block of code to run when some condition is met
# Control flow suntax makes use of colon (:) and indentation
# if some_condition:
#   execute some code
# elif some other condition:
#   do something different
# else:
# do something else

hungry = False

if hungry:
    print('Give something to eat!')
else:
    print('I am not hungry!!')

# another example
location = 'bank'
if location == 'auto shop':
    print('cars are cool!')
elif location == 'bank':
    print('withdraw some money!')
elif location == 'store':
    print('buy some grocery!')
else:
    print("I don't know much")

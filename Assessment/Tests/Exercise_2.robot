#Exercises:- 2
#Create a user defined keyword to calculate sum of the 3 numbers provided as arguments.
#Example of user defined keyword with argument and return value
#In Test case file
#Test div operation
#         ${result} =    Division Operation${number1}${number2}
#         LogThe result of ${number1} divided by ${number2} is ${result}
#In Resource file
#Define Division Operation like
#Division Operation
#[Arguments]${number1}${number2}
#${result}=Evaluate${number1}/${number2}
#[Return]${result}

*** Settings ***
*** Keywords ***
Addition
    [Arguments]  ${number1}  ${number2}  ${number3}
    ${result} =  evaluate   ${number1}+${number2}+${number3}
    [Return]  ${result}

*** Variables ***
${number1} =  1
${number2} =  2
${number3} =  3

*** Test Cases ***
Add numbers

    ${result} =  Addition   ${number1}   ${number2}  ${number3}
    log to console  addtion of 3 numbers is ${result}


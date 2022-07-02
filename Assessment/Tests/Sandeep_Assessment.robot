*** Settings ***
Library    Dialogs
Library    Collections

*** Keywords ***
Addition
    [Arguments]  ${number1}  ${number2}  ${number3}
    ${result} =  evaluate   ${number1}+${number2}+${number3}
    [Return]  ${result}

*** Variables ***
 ${number} =  2
 ${number1} =  1
 ${number2} =  2
 ${number3} =  3
 @{list} =    create list    1    2    3    4    5


*** Test Cases ***
TC001 Excercise 1
    [Tags]  excercise1
    run keyword if  ${number} > 20  log to console  number is greater than 20
    run keyword if  ${number} < 20  log to console  number is less than 20



TC002 Excercise 2
    [Tags]    excercise2
    ${result} =  Addition   ${number1}   ${number2}  ${number3}
    log to console  addtion of 3 numbers is ${result}


TC003 Append List
    [Tags]      Excercise3
    ${value} =    Get Value From User    Number Please:-
    append to list    ${list}    ${value}
    log many   @{list}
# need to understand how to print appended list in log to console.

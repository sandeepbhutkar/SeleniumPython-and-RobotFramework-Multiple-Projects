#Exercises:- 3
#Create a list of 5 numbers. Take one number as input from user. Append that number to already created list
and log the whole list consisting of 6 numbers in log using Log Many keyword.
#
#Hint: - You need to import Dialogs and Collections Library
#
#From Dialogs library use keyword “get value from user “ to get the value from user
#
#Example: - ${v}get value from userInput something
#
#Then use “append to list”
#
#Example: - append to list${list}${value}

*** Settings ***
Library    Dialogs
Library    Collections

*** Variables ***
@{list} =    create list    1    2    3    4    5

*** Test Cases ***
TC003 Append List
    [Tags]      Excersice3
    ${value} =    Get Value From User    Number Please:-
    append to list    ${list}    ${value}
    log many   @{list}

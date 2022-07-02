*** Settings ***
Library     SeleniumLibrary
*** Keywords ***

*** Variables ***

*** Test Cases ***
TC001 Run Keyword

    ${variable} =  set variable    log to console
    run keyword   ${variable}   Hello world

TC002 Run Keyword IF

    [Tags]  if
    ${variable} =   set variable    yes
    run keyword if  '${variable}' == 'yes'   log to console  value found
    run keyword if  '${variable}' == 'no'    log to console  value not found

TC003
Open browser using selenuim library keywords
    [Tags]  sel
    open browser    http:\\www.google.com      chrome
    Sleep  10
    maximize browser window
    sleep  3
    close browser



*** Settings ***
Library  SeleniumLibrary
Resource  ../Resource/13_Argument_resource.robot

*** Variables ***
${url} =  http://www.newtours.demoaut.com/
${browser} =  chrome

#ALL BELOW *** KEYWORDS *** are defined in resource file.
*** Test Cases ***
TC001:Without Arguments
    Open Login page without argument

TC002:With Arguments
    [Tags]  WA
    Open Login page with argument   ${url}   ${browser}

TC003:With Return
    [tags]  return
    Open login page with return some title



*** Settings ***
Library  SeleniumLibrary
Resource    ..//Resource/18_DataDriven.robot
Suite Setup  Open HDFC LTD login page
Suite Teardown  close
Test Template  Data template

*** Test Cases ***     ${userID}       ${password}
1   1213323     dccedef
2   23232       dwdwdwd
3   9393939         ${EMPTY}


*** Keywords ***
Data template
    [Arguments]     ${userID}    ${password}
    Click on radio button
    Enter user id  ${userID}
    Enter Password  ${password}
    Click on Login button
    sleep   5
    Error message
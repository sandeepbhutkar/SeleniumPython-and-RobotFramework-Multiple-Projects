*** Settings ***
Library  SeleniumLibrary
Resource    ..//Resource/18_DataDriven.robot
Library   DataDriver   ../Data/18_Data.xlsx    sheet_name=Sheet1
#Library   DataDriver   ../Data/18_Data.csv    sheet_name=18_Data
Suite Setup  Open HDFC LTD login page
Suite Teardown  close
Test Template  Data template

*** Test Cases ***
Login using  ${userID}  and    ${password}

*** Keywords ***
Data template
    [Arguments]     ${userID}    ${password}
    Click on radio button
    Enter user id  ${userID}
    Enter Password  ${password}
    Click on Login button
    sleep   5
    Error message
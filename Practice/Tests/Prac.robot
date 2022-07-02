*** Settings ***
Resource  ../Resources/keywords.robot
*** Variables ***

*** Test Cases ***
Test Case 1
    [Documentation]  this is my first test case
    [Tags]  Smoke
    Do Something
    Do Something else

*** Settings ***
Library           SeleniumLibrary

*** Keywords ***
*** Variables ***
*** Test Cases ***
TC001:
    [Tags]  smoke
     log to console  "Hello"
     open browser  https://www.google.com/  Chrome
     input text     name:q         "Sandeep"
     element should be visible   name:q
     get title
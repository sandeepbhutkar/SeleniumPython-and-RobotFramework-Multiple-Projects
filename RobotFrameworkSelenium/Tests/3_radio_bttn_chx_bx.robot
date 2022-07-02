
#https://www.youtube.com/watch?v=AH8SimEiFSc

*** Settings ***
Library      SeleniumLibrary
*** Keywords ***
*** Variables ***
*** Test Cases ***
TC001: Test for radio buttons and checkbox
    open browser    http://www.practiceselenium.com/practice-form.html    chrome
    maximize browser window
    set selenium speed   1
    select radio button    sex  Female
    select radio button    exp  3
    select check box      name:RedTea
    select check box      xpath://input[@id='tea3']
    unselect check box     name:RedTea
    close browser
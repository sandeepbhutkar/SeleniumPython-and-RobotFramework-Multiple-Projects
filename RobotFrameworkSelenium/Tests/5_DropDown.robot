#https://www.youtube.com/watch?v=nRF53mUIceQ
*** Settings ***
Library      SeleniumLibrary
*** Variables ***
*** Keywords ***
*** Test Cases ***
TC001:Test for drop down
    Open browser     http://www.practiceselenium.com/practice-form.html    chrome
    maximize browser window
    select from list by index   id:continents   2
    select from list by label   id:continents   Antartica
    select from list by index   id:selenium_commands    2
    select from list by index   id:selenium_commands    4
    click element   id:submit
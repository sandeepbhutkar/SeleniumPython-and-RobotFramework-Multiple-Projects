*** Settings ***
Library    SeleniumLibrary
*** Test Cases ***
catch title
    open browser  https://www.google.com   chrome
    maximize browser window
    sleep  5
    ${get_title} =  get title
    log to console  ${get_title}
    close browser
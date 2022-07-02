*** Settings ***
Library     SeleniumLibrary
*** Variables ***


*** Test Cases ***
TC001 using arguments

    @{openchrome} =  create list  https://www.google.com  chrome
    my_keyword  @{openchrome}

TC002 using arguments scalar variables
    [tags]  scale
    ${url} =    set variable  https://www.google.com
    ${browser} =    set variable  chrome
    open_google  ${url}  ${browser}

TC003 Display page title
    [Tags]  title
    ${url} =    set variable  https://www.google.com
    ${browser} =    set variable  chrome
    ${get value} =  open_google  ${url}  ${browser}
    log to console  ${get value}


*** Keywords ***
my_keyword
    [Arguments]  @{openchrome}
    open browser  @{openchrome}[0]    @{openchrome}[1]
    maximize browser window
    sleep  10
    close browser

open_google
    [Arguments]  ${url}  ${browser}
    open browser    ${url}  ${browser}
    maximize browser window
    ${get_title} =      get title
    [return]  ${get_title}
    sleep  10
    close browser
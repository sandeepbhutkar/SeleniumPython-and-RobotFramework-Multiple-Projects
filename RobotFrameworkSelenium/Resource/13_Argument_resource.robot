*** Settings ***
Library  SeleniumLibrary
*** Keywords ***
Open Login page without argument
    open browser   ${url}   ${browser}
    maximize browser window

Open Login page with argument
    [Arguments]  ${url1}    ${browser2}
    open browser   ${url1}    ${browser2}
    maximize browser window

Open login page with return some title
    open browser  ${url}   ${browser}
    maximize browser window
    ${title} =  get title
    [Return]  ${title}
    log to console  ${title}
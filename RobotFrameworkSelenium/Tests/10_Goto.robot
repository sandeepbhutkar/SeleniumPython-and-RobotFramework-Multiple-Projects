#Go to
#go back
#get location

*** Settings ***
Library  SeleniumLibrary
*** Test Cases ***
Goto Goback
    open browser    https://www.google.com    chrome
    ${loc} =  get location
    log to console   ${loc}

    sleep   3

    go to    https://www.bing.com
    ${loc} =  get location
    log to console   ${loc}

    sleep   3

    go back
    ${loc} =  get location
    log to console   ${loc}

    sleep   3
    close browser


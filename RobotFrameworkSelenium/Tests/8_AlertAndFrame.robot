#https://www.youtube.com/watch?v=qAB11ABeezw&list=PLUDwpEzHYYLsCHiiihnwl3L0xPspL7BPG&index=8
*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url} =  https://testautomationpractice.blogspot.com/

${browser} =  chrome

*** Keywords ***

*** Test Cases ***
TC001: alert
    [Tags]  alert
    open browser   ${url}  ${browser}
    maximize browser window
    click element  xpath://button[contains(text(),'Click Me')]
    #handle alert   accept
    #Element Text Should Be  xpath://p[@id='demo']   You pressed OK!
    handle alert   dismiss
    sleep   5
    ${seevalue} =  Element Text Should Be      id:demo    You pressed Cancel!
    log to console  ${seevalue}
    #handle alert    leave
    Close browser

TC002: Frame
    [Tags]  frame
    open browser   https://seleniumhq.github.io/selenium/docs/api/java/index   chrome
    maximize browser window
    select frame   name:packageListFrame
    click link   xpath://li[3]//a[1]
    unselect frame

    select frame    xpath://frame[@name='packageFrame']
    click link   xpath://a[contains(text(),'CompoundMutator')]
    unselect frame

    select frame  name:classFrame
    click link   xpath://div[@class='topNav']//a[contains(text(),'Tree')]
    unselect frame

    close browser
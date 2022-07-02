*** Settings ***
Library  SeleniumLibrary
*** Test Cases ***
TC001:Tabs
    Open Browser    http://demo.automationtesting.in/Windows.html    chrome
    maximize browser window
    click element    xpath://div[@id='Tabbed']//button[@class='btn btn-info'][contains(text(),'click')]

    select window   Sakinalium | Home
    click element   xpath://li[@class='drop']//a[contains(text(),'Documentation')]
    click element    xpath://ul[@class='dropdown']//a[contains(text(),'Web')]

    close all browsers

TC002:Windows
    [Tags]   wins
    open browser    https://google.com   chrome
    maximize browser window

    open browser    http://demo.automationtesting.in   chrome
    maximize browser window

    switch browser   1
    Input Text   xpath://input[@name='q']     sandeep

    switch browser   2
    click element   id:enterimg

    close all browsers
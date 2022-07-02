
*** Settings ***
Library    SeleniumLibrary
*** Test Cases ***
TC001:Right Click
    Open Browser    http://swisnl.github.io/jQuery-contextMenu/demo.html    chrome
    open context menu   xpath://span[@class='context-menu-one btn btn-neutral']    #right click
    click element   xpath:/html/body/ul/li[1]
    handle alert   accept


    go to    https://testautomationpractice.blogspot.com/
    double click element    xpath://*[@id="HTML10"]/div[1]/button       #double click


    go to    http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html
    drag and drop   xpath://div[@id='box2']    xpath://div[@id='box104']
    drag and drop   xpath://*[@id="box2"]     xpath://*[@id="box103"]

    sleep  3

    close browser
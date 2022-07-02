*** Settings ***
Library   SeleniumLibrary
*** Test Cases ***
TC001:Capture screenshots
    open browser   https://www.google.com    chrome
    maximize browser window
    Capture Element Screenshot    xpath://*[@id="hplogo"]    C:\Users\san\PycharmProjects\Selenium\Results\logo.png
    Capture page Screenshot         C:\Users\san\PycharmProjects\Selenium\Results\page.png
    close browser

    # if path is not given , stores in projects path.
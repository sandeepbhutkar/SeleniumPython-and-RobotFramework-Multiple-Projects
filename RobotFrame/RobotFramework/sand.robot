*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url} =  https://demo.nopcommerce.com/

${browser} =  chrome

*** Keywords ***
Login
    Maximize browser window
    #page should contain image  xpath://div[@class='header-logo']//a//img
    click link  xpath: //a[contains(text(),'Log in')]
    input text  name=Email    sandeep.bhutkar@gmail.com
    input text  id=Password     aikon58n
    click element   xpath://button[contains(text(),'Log in')]

*** Test Cases ***
TC001: Login to Demo Site
    open browser   ${url}  ${browser}
    Login
    close browser
#cd\users\san\pycharmprojects\RobotFrameworkSelenium










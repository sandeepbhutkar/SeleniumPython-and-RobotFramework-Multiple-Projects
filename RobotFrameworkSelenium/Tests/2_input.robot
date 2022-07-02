#https://www.youtube.com/watch?v=srH9wZZOL_M

*** Settings ***
Library  SeleniumLibrary

*** Variables ***

*** Keywords ***

*** Test Cases ***
Verify Input text box
    open browser  https://demo.nopcommerce.com/  chrome
    maximize browser window
    Element Text Should Be   xpath://span[@class='cart-label']   Shopping cart
    title should be     nopCommerce demo store
    sleep  5
    click element       xpath://a[@class='ico-login']
    Element Should Be Visible       name:Email
    Element Should Be Enabled       name:Email
    input text   name:Email   sandeep
    clear element text    name:Email
    sleep  5

    close browser


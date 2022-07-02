*** Settings ***
Library  SeleniumLibrary
*** Keywords ***
Open HDFC LTD login page
    open browser    https://portal.hdfc.com/login    chrome
Click on radio button
     click element   xpath://a[@id='withlogin']//label[@class='radio-custom-label']
Enter user id
    [Arguments]  ${userID}
    input text  name:user_id    ${userID}

Enter Password
    [Arguments]  ${password}
    input text      id:password     ${password}
Click on Login button
    click element  xpath://button[@class='btn-common btn-login']
Error message
    Page Should Contain element      xpath://button[@class='btn-common btn-login']
close
    close browser




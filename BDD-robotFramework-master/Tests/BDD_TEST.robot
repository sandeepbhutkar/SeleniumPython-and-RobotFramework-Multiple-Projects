*** Settings ***
Library  SeleniumLibrary

*** Keywords ***
Facebook is open
    open browser  ${URL}  ${BROWSER}

User inputs userID and password
    input text  name:email  ${email}
    input text  id:pass  ${pwd}
    click button  //input[@type='submit']

user should be denied login
    close browser

*** Variables ***
${URL} =  https://www.facebook.com/
${BROWSER} =  chrome
${email} =  abc@xyz.com
${pwd} =  password

*** Test Cases ***
Login to facebook with invalid credential
    Given Facebook is open
    When User inputs userID and password
    Then user should be denied login
#robot -d ./BDD-robotFramework-master/results ./BDD-robotFramework-master/Tests/BDD_TEST.robot
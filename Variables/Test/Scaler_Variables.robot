*** Keywords ***


*** Variables ***
#scaler variable - hold only one value
${my_variable} =  Hello World

*** Test Cases ***
TC001 Variable demonstration 1

    log  ${my_variable}

TC002 Variable Local

    [Tags]  local
    ${local variable} =  set variable  hellow
    log to console  ${local variable}

*** Settings ***
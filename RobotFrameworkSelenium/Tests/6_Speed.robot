#https://www.youtube.com/watch?v=TeK_X--r1BM&list=PLUDwpEzHYYLsCHiiihnwl3L0xPspL7BPG&index=6
*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
TC001 Set Speed:
    ${getspeed} =  get selenium speed     #to get speed it will be 0
    log to console   ${getspeed}
    open browser    http://demowebshop.tricentis.com/register   chrome
    maximize browser window
    sleep  5        #wait for 5 sec  limited to this stment
    select radio button   Gender   F
    set selenium speed  3    #wait for 3 sec  for all stements below this
    input text   id:FirstName   Sandeep
    set selenium timeout   10
    input text   id:LastName    Bhutkar
    input text   id:Email   sandeep.bhutkar@gmail.com
    ${getspeed} =  get selenium speed
    log to console   ${getspeed}     ##to get speed it will be 3
    close browser
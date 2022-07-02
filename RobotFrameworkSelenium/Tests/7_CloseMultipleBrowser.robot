#https://www.youtube.com/watch?v=ulf_1Gmkfak&list=PLUDwpEzHYYLsCHiiihnwl3L0xPspL7BPG&index=7

*** Settings ***
Library  SeleniumLibrary

*** Variables ***

*** Keywords ***

*** Test Cases ***
Verify Input text box
    open browser  https://demo.nopcommerce.com/  chrome
    maximize browser window


    open browser  https://www.google.com  chrome
    maximize browser window
    #close browser          # closes only google
    close all browsers     #will close all
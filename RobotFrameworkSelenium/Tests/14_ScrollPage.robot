*** Settings ***
Library  SeleniumLibrary

*** Variables ***

*** Keywords ***


*** Test Cases ***

TC001:Scroll Page
    open browser   https://www.countries-ofthe-world.com/flags-of-the-world.html    chrome
    maximize browser window
    #execute javascript  window.scrollTo(0,2500)     #scroll till pixel 2500
    #scroll element into view   xpath://*[@id="content"]/div[2]/div[2]/table[1]/tbody/tr[86]/td[1]/img     #scroll till element
    execute javascript  window.scrollTo(0,document.body.scrollHeight)  #scroll till bottom
    sleep  3
    execute javascript  window.scrollTo(0,-document.body.scrollHeight)  #scroll till up
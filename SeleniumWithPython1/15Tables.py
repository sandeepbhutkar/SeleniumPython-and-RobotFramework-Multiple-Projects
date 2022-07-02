from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()

driver.get('https://www.w3schools.com/html/html_tables.asp')
var1=driver.find_element_by_xpath('//*[@id="customers"]/tbody/tr[1]')
print(var1.text)        #Print first row
var2=driver.find_element_by_xpath('//*[@id="customers"]/tbody/tr[2]')
print(var2.text)        #Print second row


var3=driver.find_element_by_xpath('//*[@id="customers"]/tbody/tr[2]/td[1]')
print(var3.text)         #Print value from 2nd row and 1st column



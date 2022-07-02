from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")


driver.get("http://newtours.demoaut.com/")
var1=(driver.find_elements_by_tag_name('a'))   # "a" tag is common in all the links element.
print(len(var1))        #displays number of links

for x in var1:
    print(x.text)           #displays link names


driver.find_element_by_link_text('REGISTER').click()     # click by link attribute "link text".Can also be located by other attributes
#driver.find_element_by_partial_link_text('REG').click   #case sensitive, partially we can give.
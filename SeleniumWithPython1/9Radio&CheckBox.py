from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")
driver.get('http://www.practiceselenium.com/practice-form.html')

#Radio button - find element by ID as Name would be same like GENDER.
Var=driver.find_element_by_id('sex-1').is_displayed()
print(Var)   #true is displayed
driver.find_element_by_id('sex-1').click()

#Selecting multiple checkboxs- just find both element seperately and click
driver.find_element_by_id("tea1").click()
driver.find_element_by_id("tea3").click()





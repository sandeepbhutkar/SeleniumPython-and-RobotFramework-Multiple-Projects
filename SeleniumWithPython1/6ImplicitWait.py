from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver=webdriver.Chrome(executable_path='C:\Driver\chromedriver.exe')
driver.get('http://newtours.demoaut.com/')
driver.implicitly_wait(20)
assert "Welcome: Mercury Tours" in driver.title   #verify title
driver.find_element_by_name("userName").send_keys("sandeep.bhutkar")
driver.find_element_by_name("no element").send_keys("sandeep.bhutkar")   # this will wait till 20 sec before expception is thrown in console



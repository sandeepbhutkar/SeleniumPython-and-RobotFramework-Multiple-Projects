from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")

driver.get("http://newtours.demoaut.com/")
driver.find_element_by_name("userName").send_keys("sandeep.bhutkar")
driver.find_element_by_name("password").send_keys("Sandeep38!")
driver.find_element_by_name("login").click()

#Explicit Wait

wait=WebDriverWait(driver,20)
element=wait.until(EC.element_to_be_clickable((By.XPATH,'//body//b//input[2]')))
element.click()







from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.google.com")
print(driver.title)
driver.find_element_by_name('q').send_keys("Sandeep Bhutkar")
driver.find_element_by_name('q').click()
driver.find_element(By.XPATH,"//div[@class='FPdoLc tfB0Bf']//input[@name='btnK']").click()
time.sleep(10)
driver.quit()
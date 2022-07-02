from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.redbus.in/rPool/")


driver.add_cookie({"name":"Pune"})
print(driver.get_cookies())


from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.redbus.in/rPool/")
time.sleep(5)
driver.find_element_by_link_text("BUS TICKETS")

driver.back()
time.sleep(5)

driver.forward()
time.sleep(5)
driver.refresh()
from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get('https://testautomationpractice.blogspot.com/')

driver.find_element_by_xpath('//*[@id="HTML9"]/div[1]/button').click()
time.sleep(10)
#driver.switch_to_alert().accept()
driver.switch_to_alert().accept()
#driver.switch_to_alert().dismiss()
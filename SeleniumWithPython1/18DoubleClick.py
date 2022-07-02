from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome()

driver.get('https://testautomationpractice.blogspot.com/')
var1=driver.find_element_by_xpath("//div[@id='HTML10']//div//button")
var2=ActionChains(driver)
var2.double_click(var1).click().perform()

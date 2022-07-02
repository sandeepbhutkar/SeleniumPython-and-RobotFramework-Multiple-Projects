from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome()
driver.get('http://swisnl.github.io/jQuery-contextMenu/demo.html')
var1=driver.find_element_by_xpath('/html/body/div/section/div/div/div/p/span')
var2=ActionChains(driver)
var2.context_click(var1).perform()

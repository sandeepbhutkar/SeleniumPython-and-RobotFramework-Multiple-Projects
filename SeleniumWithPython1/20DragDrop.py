from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome()

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
source=driver.find_element_by_id('box3')
target=driver.find_element_by_id('box106')

var1=ActionChains(driver)
var1.drag_and_drop(source,target).perform()
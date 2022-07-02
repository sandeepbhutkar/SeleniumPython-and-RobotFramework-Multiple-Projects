
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()

driver.get("https://jqueryui.com/resources/demos/droppable/default.html")

var1 = driver.find_element_by_xpath("//p[contains(text(),'Drag me to my target')]")
var2 = driver.find_element_by_xpath("//div[@id='droppable']")

var3 = ActionChains(driver)

#var3.drag_and_drop(var1, var2).perform()

#interview Question : other way click and hold and move to element
var3.click_and_hold(var1).move_to_element(var2).perform()
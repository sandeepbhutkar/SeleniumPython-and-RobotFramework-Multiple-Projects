from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()

driver.get("https://www.spicejet.com/")

var1 = driver.find_element_by_id("ctl00_HyperLinkLogin")
var2 = driver.find_element_by_xpath("//a[contains(text(),'SpiceClub Members')]")
var3 = driver.find_element_by_xpath("//li[@class='hide-mobile']//ul//li//a[contains(text(),'Member Login')]")

var4 = ActionChains(driver)

var4.move_to_element(var1).move_to_element(var2).move_to_element(var3).click().perform()
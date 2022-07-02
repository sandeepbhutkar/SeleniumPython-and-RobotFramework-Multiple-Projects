from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

driver=webdriver.Chrome()

driver.get('https://opensource-demo.orangehrmlive.com/')
driver.find_element_by_id('txtUsername').send_keys('Admin')
driver.find_element_by_id('txtPassword').send_keys('admin123')
driver.find_element_by_id('btnLogin').click()

#find xpath of "Admin tab", than 'User', than 'User Management' and store them im variable.
var1=driver.find_element_by_xpath("//a[@id='menu_admin_viewAdminModule']//b")
var2=driver.find_element_by_xpath("//a[@id='menu_admin_UserManagement']")
var3=driver.find_element_by_xpath("//a[@id='menu_admin_viewSystemUsers']")

var4=ActionChains(driver)
var4.move_to_element(var1).move_to_element(var2).move_to_element(var3).click().perform()
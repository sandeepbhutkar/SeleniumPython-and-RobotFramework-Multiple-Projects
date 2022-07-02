from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_xpath("//input[@class='button']").click()
#u can create your own xpath using above pattern , u can give other attributes as well like class,value,id,name.


from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/")
#By CSS Selectors
driver.find_element_by_css_selector("#txtUsername").send_keys("Admin")  #by # id
driver.find_element_by_css_selector("input[name=txtPassword").send_keys("admin123")  # by input name
#driver.find_element_by_css_selector(".button").click()  #by .class

#By Class name
driver.find_element_by_class_name("button").click()
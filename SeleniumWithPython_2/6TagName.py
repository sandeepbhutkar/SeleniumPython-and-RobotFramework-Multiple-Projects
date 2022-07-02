from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
var1 = driver.find_element_by_tag_name("h1")   # Header
print(var1.text)


#result is "Automation Testing Practice"

from selenium import webdriver

var1 = webdriver.ChromeOptions()
var1.headless = True
driver = webdriver.Chrome(options=var1)

driver.get("https://www.redbus.in/rPool/")
print(driver.title)
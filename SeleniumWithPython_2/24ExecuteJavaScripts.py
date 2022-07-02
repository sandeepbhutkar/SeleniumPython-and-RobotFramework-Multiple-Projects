from selenium import webdriver
import time
driver = webdriver.Chrome()

driver.get("https://www.amazon.in/")

var1 = driver.execute_script("return document.title")   # in java script we write document.title to get title.
print(var1)

time.sleep(10)
driver.execute_script("history.go(0);")   #refresh page

var2 = driver.execute_script("return document.documentElement.innerText")
print(var2)
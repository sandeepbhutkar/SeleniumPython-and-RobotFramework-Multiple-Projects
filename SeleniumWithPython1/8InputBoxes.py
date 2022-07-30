from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



driver=webdriver.Chrome("C:\Driver\chromedriver.exe")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
textbox=driver.find_elements_by_class_name("text_field")
#find element's' is used to capture multiple elements. and find elemen't' for single.

print(len(textbox))

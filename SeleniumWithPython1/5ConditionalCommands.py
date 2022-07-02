from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")


driver.get("http://newtours.demoaut.com/")

user_ele=driver.find_element_by_name("userName")
print(user_ele.is_displayed())
print(user_ele.is_enabled())

user_ele.send_keys("sandeep.bhutkar")
user_pass=driver.find_element_by_name("password")
user_pass.send_keys("Sandeep38!")

driver.find_element_by_name("login").click()

roundtrip=driver.find_element_by_css_selector("input[value=roundtrip]")
print("Status of round trip radio button is:" , roundtrip.is_selected())

oneway=driver.find_element_by_css_selector("input[value=oneway]")
print("Status of one way radio button is:" ,oneway.is_selected())


####below also works for radio button
#roundtrip=driver.find_element_by_xpath("//body//b//input[1]")
#print(roundtrip.is_selected())




from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://mail.rediff.com/cgi-bin/login.cgi")

driver.find_element_by_class_name("signinbtn").click()

var1 = driver.switch_to.alert
print(var1.text)         # capture it before accepting, other wise if u capture text after accept() how it will capture.
#driver.switch_to.alert.dismiss()   # Cancel
var1.accept()   #OK

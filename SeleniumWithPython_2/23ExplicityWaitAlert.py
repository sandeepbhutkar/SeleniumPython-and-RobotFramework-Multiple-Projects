from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
driver.find_element_by_css_selector("input[title='Sign in']").click()


wait = WebDriverWait(driver, 20)
var1 = wait.until(EC.alert_is_present())

var1 = driver.switch_to.alert
print(var1.text)
var1.accept()



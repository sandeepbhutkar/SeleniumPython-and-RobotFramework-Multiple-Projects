from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://the-internet.herokuapp.com/javascript_alerts")

driver.find_element_by_css_selector("button[onclick='jsPrompt()'").click()

driver.switch_to.alert.send_keys("Sandeep")



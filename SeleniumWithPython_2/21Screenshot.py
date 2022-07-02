from selenium import webdriver

var1 = webdriver.ChromeOptions()
var1.headless = True
driver = webdriver.Chrome(options=var1)

driver.get("https://www.redbus.in/rPool/")

driver.get_screenshot_as_file("redbus_screenshot.png")

#Full screenshot     # for taking full SS , exe. should be always headless.

S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width'), S('Height'))
driver.find_element_by_tag_name('body').screenshot('redbus_full_screenshot.png');
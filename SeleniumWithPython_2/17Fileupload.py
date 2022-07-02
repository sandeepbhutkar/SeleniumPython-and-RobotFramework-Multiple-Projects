from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://cgi-lib.berkeley.edu/ex/fup.html")

driver.find_element_by_css_selector("input[type='file']").send_keys("C://Users/san/PycharmProjects/RobotFrameworkSelenium/Tests/1_Login.robot")
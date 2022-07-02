from selenium import  webdriver

driver=webdriver.Chrome()

driver.get("https://www.flipkart.com/")

#driver.save_screenshot("F:\RobotFrameworkSelenium With Python\screenshot.jpg")
driver.get_screenshot_as_file("F:\Selenium With Python\screenshot1.jpg")

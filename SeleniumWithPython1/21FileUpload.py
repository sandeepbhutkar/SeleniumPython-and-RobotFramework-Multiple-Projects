from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.switch_to.frame(0)  # as there is only one frame , hence 0 , 0 is index
driver.find_element_by_id("RESULT_FileUpload-10").send_keys("C://Users/san/PycharmProjects/RobotFrameworkSelenium/Tests/1_Login.robot")
#upload button - find element by id,name etc and in send keys give path of file to be uploaded (remember bacward slash to give)
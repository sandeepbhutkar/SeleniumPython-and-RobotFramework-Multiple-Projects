from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver=webdriver.Chrome()

driver.get('https://www.selenium.dev/selenium/docs/api/java/')
driver.switch_to_frame('packageListFrame')
driver.find_element_by_link_text('com.thoughtworks.selenium').click()
driver.switch_to_default_content()
driver.switch_to_frame('packageFrame')
driver.find_element_by_link_text('Wait').click()
driver.switch_to_default_content()
driver.switch_to_frame('classFrame')
driver.find_element_by_xpath('/html/body/div[1]/ul/li[5]').click()

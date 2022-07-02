from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver=webdriver.Chrome()
driver.get('http://demo.automationtesting.in/Windows.html')
driver.execute_script("window.open('http://www.twitter.com', 'new window')")
driver.switch_to.window(driver.window_handles[0])
driver.get("https://www.google.com")
driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input').send_keys('Sandeep')
driver.switch_to.window(driver.window_handles[1])

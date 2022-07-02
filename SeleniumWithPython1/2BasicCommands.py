from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")

driver.get("http://demo.automationtesting.in/Windows.html")
print(driver.title)
print(driver.current_url)

driver.find_element_by_xpath("//div[@id='Tabbed']//button[@class='btn btn-info'][contains(text(),'click')]").click()
time.sleep(10)
#driver.close()  #current browser/tab will close
driver.quit()     #all browser /tabs will be closed

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(executable_path='C:\Driver\chromedriver.exe')
#driver=webdriver.Firefox(executable_path='C:\Driver\geckodriver.exe')
#driver=webdriver.Ie(executable_path='C:\Driver\IEDriverServer.exe')

driver.get("http://newtours.demoaut.com/")
driver.maximize_window()
print(driver.title)  #Get Title of the page
#print(driver.page_source)    # HTML code of page
print(driver.current_url)  #url
driver.close()   # Close the browser

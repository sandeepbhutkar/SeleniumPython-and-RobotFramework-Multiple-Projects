from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chromeOptions=Options()
chromeOptions.add_experimental_option("prefs",{"download.default_directory": "F:\Selenium With Python"})
#abobe 3 line code is only needed if uwant to dowunlad at perticular location.
# by default scppirt will downlod at default loaction .Default loaction can also be chaged from crome settings.


driver=webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe",chrome_options=chromeOptions)
driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.find_element_by_id("textbox").send_keys("Testing")
driver.find_element_by_id("createTxt").click()
driver.find_element_by_id("link-to-download").click()


#same code can be used to download any type of file.
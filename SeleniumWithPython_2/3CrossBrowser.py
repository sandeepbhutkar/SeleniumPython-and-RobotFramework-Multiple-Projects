#pip install webdriver-manager
#this will install driver in cache when u run script first time. second time it will not
#There are 3 ways i understood now to open call driver .1) executable path 2) put exe. in Python>Script file
#3) wedriver manager which will install exe in cache.
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager



browserName = "chrome"   #update browser as u want.

if browserName == "chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browserName == "firefox":
     driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif browserName == "safari":
     driver = webdriver.Safari()
else:
    print("Enter correct browser name")

driver.get("https://www.google.com")
driver.quit()
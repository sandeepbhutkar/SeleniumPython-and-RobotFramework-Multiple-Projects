from selenium import webdriver

driver=webdriver.Chrome()            # if chromedriver.exe is there in Script folder of Python, not need to give executable path
driver.get('http://newtours.demoaut.com/')
try:
    assert "Welcome: Mercury Tourss" in driver.title   # verify title
    print('Pass')
except:
    print('fail')

    #try and except will verify block of code.
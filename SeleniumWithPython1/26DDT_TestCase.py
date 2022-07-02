import DDT_Functions
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://newtours.demoaut.com/")
driver.maximize_window()
path="F:\Selenium With Python\Data.xlsx"
rows=DDT_Functions.getRowCount(path,"Sheet1")
for r in range(2,rows+1):
    username=DDT_Functions.readData(path,"Sheet1",r,1)
    password=DDT_Functions.readData(path,"Sheet1",r,2)
    driver.find_element_by_name("userName").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("login").click()
    if driver.title=="Find a Flight: Mercury Tours:":
        DDT_Functions.WriteData(path,"Sheet1",r,3,"Passed")
    else:
        DDT_Functions.WriteData(path,"Sheet1",r,3,"Fails")
    driver.find_element_by_link_text("Home").click()




from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")

# def myfuct(element,index):
#     Select(driver.find_element_by_id(element)).select_by_index(index)
#
# myfuct('speed', '2')
# myfuct('files', '2')
# Select(driver.find_element_by_id("speed")).select_by_index(2)
# Select(driver.find_element_by_id("files")).select_by_index(2)
# lets suppose there are multiple drop down , so instead of writing multiple time select statement , write fuction/

#Print lenght

# var1 = Select(driver.find_element_by_id("speed"))
# print(len(var1.options))          # remember var1.options

#print drop down values
# for i in var1.options:                    # remember var1.options
#     print(i.text)
#     if(i.text == "Medium"):
#         break

# to find lenth with out using Select use xpath (interview Question)
var3 = driver.find_element_by_xpath("//select[@id='speed']/option")
print(len(var3))
for i in var3:
    print(i)
from selenium import webdriver

driver=webdriver.Chrome()

driver.get("https://www.flipkart.com/")
#1)len
var1=driver.get_cookies()    # get cookies in var
print(var1)          #print cookies name   list format , dictional list name and value
print(len(var1))   # print cookies count
#2)Add
driver.add_cookie({'name':'Sandeep','value':'123456'})
var1=driver.get_cookies()
print(var1)
#3)Delete perticular cookie by name
driver.delete_cookie('name')
var1=driver.get_cookies()
print(var1)
#4)Delete all cookies
driver.delete_all_cookies()
var1=driver.get_cookies()
print(var1)
print(len(var1))   # 0

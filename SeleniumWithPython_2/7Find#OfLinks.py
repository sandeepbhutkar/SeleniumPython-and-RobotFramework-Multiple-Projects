from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
var1 = driver.find_elements_by_tag_name("a")
print(len(var1))
for i in var1:
    print(i.text)

# to find all images

var2 = driver.find_elements_by_tag_name("img")
print(len(var2))
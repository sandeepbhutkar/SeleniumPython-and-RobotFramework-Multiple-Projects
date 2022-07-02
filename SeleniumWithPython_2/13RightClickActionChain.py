from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")

var1 = driver.find_element_by_xpath("//span[@class='context-menu-one btn btn-neutral']")

var2 = ActionChains(driver)

var2.context_click(var1).perform()

#driver.find_element_by_xpath("//li[@class='context-menu-item context-menu-icon context-menu-icon-edit']").click()
#other option to Click

var3 = driver.find_elements_by_css_selector("li.context-menu-icon span")      #tag li + class
for i in var3:
    print(i.text)
    if i.text == "Cut":
        i.click()
        break

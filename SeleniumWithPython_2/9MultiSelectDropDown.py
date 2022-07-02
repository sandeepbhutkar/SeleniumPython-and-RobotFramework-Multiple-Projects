from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")
driver.find_element_by_id("justAnInputBox").click()
var1 = driver.find_elements_by_css_selector("span.comboTreeItemTitle")

print(len(var1))

for i in var1:
    print(i.text)
    if i.text == "choice 2":
        i.click()
    elif i.text == "choice 6 1":
        i.click()

driver.close()
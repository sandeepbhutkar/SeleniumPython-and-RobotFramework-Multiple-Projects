from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")
driver.find_element_by_id("justAnInputBox").click()
var1 = driver.find_elements_by_css_selector("span.comboTreeItemTitle")

def function(value):
    for i in var1:
        if i.text == value:
            i.click()
            break    # no need, but to increace performance use it


function("choice 2")
function("choice 6 1")
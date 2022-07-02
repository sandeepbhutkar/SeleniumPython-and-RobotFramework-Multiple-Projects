from selenium import webdriver
from selenium.webdriver.support.ui import Select


driver=webdriver.Chrome()
driver.get('http://www.practiceselenium.com/practice-form.html')

Select(driver.find_element_by_id('continents')).select_by_index(2)
# Select(driver.find_element_by_id('continents')).select_by_value('')  #from HTML code
# Select(driver.find_element_by_id('continents')).select_by_visible_text('Antartica')

# to find count
# var1=Select(driver.find_element_by_id('continents'))
# print(len(var1.options))

# to print all values from dropdown
# var1=Select(driver.find_element_by_id('continents'))
# for x in var1.options:
#     print(x.text)



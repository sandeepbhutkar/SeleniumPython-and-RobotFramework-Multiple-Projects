#Data Driven + Write data emp id from UI to excel.

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import DDTFunction


driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get('https://opensource-demo.orangehrmlive.com/')
driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_css_selector(".button").click()
path = "C:/Users/san/PycharmProjects/E2E_Selenium_Python2ReadWrite/Data/Data_E2E_Selenium_Python2.xlsx"
row = DDTFunction.getRowCount(path, "Sheet1")
print(row)
for r in range(2, row + 1):
    var1 = driver.find_element_by_xpath("//b[contains(text(),'PIM')]")
    var2 = driver.find_element_by_xpath("//a[@id='menu_pim_addEmployee']")
    var3 = ActionChains(driver)
    var3.move_to_element(var1).move_to_element(var2).click().perform()
    FirstName = DDTFunction.readData(path, "Sheet1", r, 1)
    LastName = DDTFunction.readData(path, "Sheet1", r, 2)
    driver.find_element_by_id("firstName").send_keys(FirstName)
    driver.find_element_by_id("lastName").send_keys(LastName)
    var4 = driver.find_element_by_id("employeeId").get_attribute('value')
    print(var4)
    DDTFunction.WriteData(path, "Sheet1", r, 3, var4)
driver.close()


from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from E2E_Pytest_HTML.Resources import ExcelFunction

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

#Login
driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
driver.find_element_by_id("Email").clear()
driver.find_element_by_id("Email").send_keys("admin@yourstore.com")
driver.find_element_by_id("Password").clear()
driver.find_element_by_id("Password").send_keys("admin")
driver.find_element_by_css_selector(".button-1.login-button").click()

#Data Driven
path = "C:/Users/sbhutkar/PycharmProjects/pythonProject/E2E_Pytest_HTML/Data/DataSheet.xlsx"
row = ExcelFunction.GetRow(path, "Sheet1")
for r in range(2, row+1):
    Email = ExcelFunction.ReadRow(path, "Sheet1", r, 2)
    Password = ExcelFunction.ReadRow(path, "Sheet1", r, 3)
    First_Name = ExcelFunction.ReadRow(path, "Sheet1", r, 4)
    Last_Name = ExcelFunction.ReadRow(path, "Sheet1", r, 5)
    Gender = ExcelFunction.ReadRow(path, "Sheet1", r, 6)
    Vendor = ExcelFunction.ReadRow(path, "Sheet1", r, 8)
    # CLick on Customer
    driver.find_element_by_css_selector(".fa.fa-user").click()
    driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/ul/li[4]/ul/li[1]/a/span").click()
    # Add New Customer
    driver.find_element_by_class_name("btn.bg-blue").click()
    driver.find_element_by_xpath("//*[@id='customer-info']").click()
    driver.find_element_by_id("Email").send_keys(Email)
    driver.find_element_by_id("Password").send_keys(Password)
    driver.find_element_by_id("FirstName").send_keys(First_Name)
    driver.find_element_by_id("LastName").send_keys(Last_Name)
    driver.find_element_by_id(Gender).click()
    driver.find_element_by_id("DateOfBirth").send_keys("9/9/1999")
    Select(driver.find_element_by_id("VendorId")).select_by_index(Vendor)
    driver.find_element_by_css_selector("button[name='save']").click()
    #Search
    driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/ul/li[4]/ul/li[1]/a/span").click()
    driver.find_element_by_id("SearchEmail").send_keys(Email)
    driver.find_element_by_id("search-customers").click()
    #Verify EMail ID.
    var2 = driver.find_element_by_xpath("//*[@id='customers-grid']/tbody/tr/td[2]").text
    assert Email == var2
    #Write Data
    var3 = driver.find_element_by_xpath("//*[@id='customers-grid']/tbody/tr/td[4]").text
    ExcelFunction.WriteData(path, "Sheet1", r, 9, var3)
    #Read Written data from excel and pass to UI
    Customer_Role = ExcelFunction.ReadRow(path, "Sheet1", r, 9)
    driver.find_element_by_id("SearchEmail").clear()
    driver.find_element_by_id("SearchEmail").send_keys(Customer_Role)
    driver.find_element_by_id("search-customers").click()
driver.close()





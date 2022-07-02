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

#time.sleep(10)

path = "C:/Users/sbhutkar/PycharmProjects/pythonProject/E2E_Pytest_HTML/Data/DataSheet.xlsx"
row = ExcelFunction.GetRow(path, "Sheet1")
for r in range(2, row+1):
    Email = ExcelFunction.ReadRow(path, "Sheet1", r, 2)
    Password = ExcelFunction.ReadRow(path, "Sheet1", r, 3)
    First_Name = ExcelFunction.ReadRow(path, "Sheet1", r, 4)
    Last_Name = ExcelFunction.ReadRow(path, "Sheet1", r, 5)
    Gender = ExcelFunction.ReadRow(path, "Sheet1", r, 6)
    #DOB = ExcelFunction.ReadRow(path, "Sheet1", r, 7)
    Vendor = ExcelFunction.ReadRow(path, "Sheet1", r, 8)
    # Customer
    driver.find_element_by_css_selector(".fa.fa-user").click()
    driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/ul/li[4]/ul/li[1]/a/span").click()
    # Add New Customer
    driver.find_element_by_class_name("btn.bg-blue").click()
    driver.find_element_by_xpath("//*[@id='customer-info']").click()
#var1 = "test9@test.com"
    driver.find_element_by_id("Email").send_keys(Email)
#print(var1)
    driver.find_element_by_id("Password").send_keys(Password)
    driver.find_element_by_id("FirstName").send_keys(First_Name)
    driver.find_element_by_id("LastName").send_keys(Last_Name)
    driver.find_element_by_id(Gender).click()
    #driver.find_element_by_id("DateOfBirth").click()
    driver.find_element_by_id("DateOfBirth").send_keys("9/9/1999")
    Select(driver.find_element_by_id("VendorId")).select_by_index(Vendor)
    time.sleep(10)
    #driver.refresh()
    driver.find_element_by_css_selector("button[name='save']").click()
    #Search
    driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/ul/li[4]/ul/li[1]/a/span").click()
    driver.find_element_by_id("SearchEmail").send_keys(Email)
    driver.find_element_by_id("search-customers").click()
    #Verify EMail ID.
    var2 = driver.find_element_by_xpath("//*[@id='customers-grid']/tbody/tr/td[2]").text
    var3 = driver.find_element_by_xpath("//*[@id='customers-grid']/tbody/tr/td[4]").text
    #print(var3)
    ExcelFunction.WriteData(path, "Sheet1", r, 9, var3)
    Customer_Role = ExcelFunction.ReadRow(path, "Sheet1", r, 9)
    driver.find_element_by_id("SearchEmail").clear()
    driver.find_element_by_id("SearchEmail").send_keys(Customer_Role)
    driver.find_element_by_id("search-customers").click()
    # var4 = driver.find_element_by_xpath("//*[@id='customers-grid']/tbody/tr/td").text
    # print(var4)
    assert Email == var2
    time.sleep(5)
driver.close()


#driver.find_element_by_xpath("//*[@id='customer-info']/div[2]/div[1]/div[10]/div[2]/div/div[1]/divv").click()
#driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_listbox']/li[3]").click()


# var1 = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/form/div[2]/ul/li").text
#var2 = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[1]")
#print(var2.text)
#assert (var2.text) == "The new customer has been added successfully."

#print(var2)
#if var2.text == "The new customer has been added successfully.":
#     print("Test Passed")
#else:
#     print("Test Failed")
#Search

#

# #tommorow find the email id in table and verify it....

# #var2 = driver.find_element_by_xpath("//*[@id='customers-grid']/tbody/tr")
# #//*[@id="customers-grid"]/tbody/tr/td[2]
#print(var2.text)

#




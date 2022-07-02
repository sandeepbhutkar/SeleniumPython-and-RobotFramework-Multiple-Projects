from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

from E2E.Resources import ExcelFunctions
driver = webdriver.Chrome()
driver.implicitly_wait(10)
#Login
driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_name("Submit").click()

#ActionChains
var1 = driver.find_element_by_xpath("//*[@id='menu_leave_viewLeaveModule']/b")
var2 = driver.find_element_by_id("menu_leave_viewLeaveList")
var3 = ActionChains(driver)
var3.move_to_element(var1).move_to_element(var2).click().perform()

driver.find_element_by_id("calFromDate").clear()
driver.find_element_by_id("calFromDate").send_keys("2020-02-02")
driver.find_element_by_id("calToDate").clear()
driver.find_element_by_id("calToDate").send_keys("2020-02-02")


path = "C:/Users/sbhutkar/PycharmProjects/pythonProject/E2E/Data/TestData.xlsx"
row = ExcelFunctions.GetRowCount(path, "Sheet1")
for r in range(2, row + 1):
    Leaves_Status = ExcelFunctions.ReadData(path, "Sheet1", r, 1)
    Sub_Unit = ExcelFunctions.ReadData(path, "Sheet1", r, 2)
    driver.find_element_by_id(Leaves_Status).click()
    Select(driver.find_element_by_id("leaveList_cmbSubunit")).select_by_visible_text(Sub_Unit)
    # Select text to write in excel
    var4 = driver.find_element_by_xpath("//*[@id='frmFilterLeave']/fieldset/ol/li[6]/label").text
    ExcelFunctions.WriteData(path, "Sheet1", r, 3, var4)



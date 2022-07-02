from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import unittest
import HtmlTestRunner
import ExcelFunctions
#from E2E_Testing.Resources import ExcelFunctions   # not working from CMD

class OrangeHRM_Regression(unittest.TestCase):
    def test_Leaves_Workflow1(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        # Login
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_name("Submit").click()

        # ActionChains
        var1 = self.driver.find_element_by_xpath("//*[@id='menu_leave_viewLeaveModule']/b")
        var2 = self.driver.find_element_by_id("menu_leave_viewLeaveList")
        var3 = ActionChains(self.driver)
        var3.move_to_element(var1).move_to_element(var2).click().perform()

        self.driver.find_element_by_id("calFromDate").clear()
        self.driver.find_element_by_id("calFromDate").send_keys("2020-02-02")
        self.driver.find_element_by_id("calToDate").clear()
        self.driver.find_element_by_id("calToDate").send_keys("2020-02-02")

        path = "C:/Users/sbhutkar/PycharmProjects/pythonProject/E2E/Data/TestData.xlsx"
        row = ExcelFunctions.GetRowCount(path, "Sheet1")
        for r in range(2, row + 1):
            Leaves_Status = ExcelFunctions.ReadData(path, "Sheet1", r, 1)
            Sub_Unit = ExcelFunctions.ReadData(path, "Sheet1", r, 2)
            self.driver.find_element_by_id(Leaves_Status).click()
            Select(self.driver.find_element_by_id("leaveList_cmbSubunit")).select_by_visible_text(Sub_Unit)
            # Select text to write in excel
            var4 = self.driver.find_element_by_xpath("//*[@id='frmFilterLeave']/fieldset/ol/li[6]/label").text
            ExcelFunctions.WriteData(path, "Sheet1", r, 3, var4)

    def test_Leaves_Workflow2(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        # Login
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_name("Submit").click()

        # ActionChains
        var1 = self.driver.find_element_by_xpath("//*[@id='menu_leave_viewLeaveModule']/b")
        var2 = self.driver.find_element_by_id("menu_leave_viewLeaveList")
        var3 = ActionChains(self.driver)
        var3.move_to_element(var1).move_to_element(var2).click().perform()

        self.driver.find_element_by_id("calFromDate").clear()
        self.driver.find_element_by_id("calFromDate").send_keys("2020-02-02")
        self.driver.find_element_by_id("calToDate").clear()
        self.driver.find_element_by_id("calToDate").send_keys("2020-02-02")

        path = "C:/Users/sbhutkar/PycharmProjects/pythonProject/E2E/Data/TestData.xlsx"
        row = ExcelFunctions.GetRowCount(path, "Sheet1")
        for r in range(2, row + 1):
            Leaves_Status = ExcelFunctions.ReadData(path, "Sheet1", r, 1)
            Sub_Unit = ExcelFunctions.ReadData(path, "Sheet1", r, 2)
            self.driver.find_element_by_id(Leaves_Status).click()
            Select(self.driver.find_element_by_id("leaveList_cmbSubunit")).select_by_visible_text(Sub_Unit)
            # Select text to write in excel
            var4 = self.driver.find_element_by_xpath("//*[@id='frmFilterLeave']/fieldset/ol/li[6]/label").text
            ExcelFunctions.WriteData(path, "Sheet1", r, 3, var4)
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/sbhutkar/PycharmProjects/pythonProject/E2E_Testing/Reports"))





#Data Driven + Write data emp id from UI to excel.
#import C:\\Users\\san\\PycharmProjects\\E2E_Selenium_Python2ReadWrite\\Resourses\\DDTFunction.py
import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import DDTFunction

class Regression_Test_Willis(unittest.TestCase):
    def test_EmployeeCreation(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.driver.get('https://opensource-demo.orangehrmlive.com/')
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_css_selector(".button").click()
        path = "C:/Users/san/PycharmProjects/E2E_Selenium_Python2ReadWrite/Data/Data_E2E_Selenium_Python2.xlsx"
        row = DDTFunction.getRowCount(path, "Sheet1")
        for r in range(2, row + 1):
            var1 = self.driver.find_element_by_xpath("//b[contains(text(),'PIM')]")
            var2 = self.driver.find_element_by_xpath("//a[@id='menu_pim_addEmployee']")
            var3 = ActionChains(self.driver)
            var3.move_to_element(var1).move_to_element(var2).click().perform()
            FirstName = DDTFunction.readData(path, "Sheet1", r, 1)
            LastName = DDTFunction.readData(path, "Sheet1", r, 2)
            self.driver.find_element_by_id("firstName").send_keys(FirstName)
            self.driver.find_element_by_id("lastName").send_keys(LastName)
            var4 = self.driver.find_element_by_id("employeeId").get_attribute('value')
            DDTFunction.WriteData(path, "Sheet1", r, 3, var4)
        self.driver.close()
        print("Test Passed for Employee")

    def test_EmployerCreation(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.driver.get('https://opensource-demo.orangehrmlive.com/')
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_css_selector(".button").click()
        path = "C:/Users/san/PycharmProjects/E2E_Selenium_Python2ReadWrite/Data/Data_E2E_Selenium_Python2.xlsx"
        row = DDTFunction.getRowCount(path, "Sheet1")
        for r in range(2, row + 1):
            var1 = self.driver.find_element_by_xpath("//b[contains(text(),'PIM')]")
            var2 = self.driver.find_element_by_xpath("//a[@id='menu_pim_addEmployee']")
            var3 = ActionChains(self.driver)
            var3.move_to_element(var1).move_to_element(var2).click().perform()
            FirstName = DDTFunction.readData(path, "Sheet1", r, 1)
            LastName = DDTFunction.readData(path, "Sheet1", r, 2)
            self.driver.find_element_by_id("firstName").send_keys(FirstName)
            self.driver.find_element_by_id("lastName").send_keys(LastName)
            var4 = self.driver.find_element_by_id("employeeId").get_attribute('value')
            DDTFunction.WriteData(path, "Sheet1", r, 3, var4)
        self.driver.close()
        print("Test Passed for Employer")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/san/PycharmProjects/E2E_Selenium_Python2ReadWrite/Reports"))


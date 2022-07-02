from selenium import webdriver
import HtmlTestRunner
from selenium.webdriver.support.ui import Select
import DDFunctions
import unittest

class E2ETest(unittest.TestCase):        #create class
    def test_Test1(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://newtours.demoaut.com/")
        self.driver.maximize_window()
        path = "F:\Selenium With Python\DataE2E.xlsx"
        rows = DDFunctions.getRowCount(path, "Sheet1")
        for r in range(2, rows + 1):
            username = DDFunctions.readData(path, "Sheet1", r, 1)
            password = DDFunctions.readData(path, "Sheet1", r, 2)
            firstname = DDFunctions.readData(path, "Sheet1", r, 3)
            lastname = DDFunctions.readData(path, "Sheet1", r, 4)
            number = DDFunctions.readData(path, "Sheet1", r, 5)
            self.driver.find_element_by_name("userName").send_keys(username)
            self.driver.find_element_by_name("password").send_keys(password)
            self.driver.find_element_by_name("login").click()
            Select(self.driver.find_element_by_name("passCount")).select_by_index(3)
            self.driver.find_element_by_xpath("//body//font//font//input[1]").click()
            self.driver.find_element_by_name("findFlights").click()
            self.driver.find_element_by_name("reserveFlights").click()
            self.driver.find_element_by_name("passFirst0").send_keys(firstname)
            self.driver.find_element_by_name("passLast0").send_keys(lastname)
            self.driver.find_element_by_name("creditnumber").send_keys(number)
            self.driver.find_element_by_name("buyFlights").click()
            var1 = self.driver.find_element_by_xpath("//body//p//font//font[2]")
            print(var1.text)
            self.driver.find_element_by_xpath("//body//p//font//font[2]").is_displayed()
            self.driver.find_element_by_link_text("Home").click()

    def test_Test2(self):
        print("hello")
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/san/PycharmProjects/E2E_Selenium_Python'))
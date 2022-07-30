import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from pageObjects.CustomerPage import customer_page
from Utilities import XLUtils
import logging

class Test_CreateCustData:
    Url = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    Email = "admin@yourstore.com"
    Password = "admin"
    Path = "./TestData/LoginData.xlsx"
    Rows = XLUtils.GetRowCount(Path, "Sheet1")

    def test_createcustdata(self):
        logging.info("Data Creation Test Case Start")
        for r in range(2, self.Rows+1):
            self.driver = webdriver.Chrome(executable_path="C://Driver//chromedriver.exe")
            self.driver.implicitly_wait(30)
            self.driver.get(self.Url)
            self.driver.maximize_window()
            # Login Page
            self.lp = LoginPage(self.driver)
            self.lp.Enter_Email(self.Email)
            self.lp.Enter_Password(self.Password)
            self.lp.Click_Login()
            # Add New Customer
            self.cp = customer_page(self.driver)
            self.cp.Click_Customer_Link()
            self.cp.Click_Customer_SubLink()
            self.cp.Click_AddNew()
            #ReadData from Excel
            self.cp.Enter_Email(XLUtils.ReadData(self.Path, "Sheet1", r, 1))
            self.cp.Click_Save()
            #WriteData in Excel
            self.WriteData = self.cp.capture_Email()
            XLUtils.WriteData(self.Path, "Sheet1", r, 2, self.WriteData)
            self.driver.close()
        logging.info("Test Data created in Excel")

    #pytest -v -m smoke --html=Reports/Report.html testCase/test_CreateCustData.py
    @pytest.mark.smoke
    def test_verify_login_sucess(self):
        self.driver = webdriver.Chrome(executable_path="C://Driver//chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.driver.get(self.Url)
        self.driver.maximize_window()

        # Login Page
        self.lp = LoginPage(self.driver)
        self.lp.Enter_Email(self.Email)
        self.lp.Enter_Password(self.Password)
        self.lp.Click_Login()

        if self.driver.title == "Dashboard / nopCommerce administration":
            assert True
        else:
            self.driver.save_screenshot("./Screenshots/LoginPage.png")
            assert False
        self.driver.close()





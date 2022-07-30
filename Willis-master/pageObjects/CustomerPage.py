from selenium.webdriver.common.by import By

class customer_page:
    Link_Customer1_Xpath = "//body/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[4]/a[1]"
    Link_Customer2_Xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p"
    Btn_AddNew_Xpath = "//body/div[3]/div[1]/form[1]/div[1]/div[1]/a[1]"
    Txt_Email_Id = "Email"
    Btn_Save_Name = "save"
    Txt_Table_Xpath = "XPATH"

    def __init__(self,driver):
        self.driver = driver

    def Click_Customer_Link(self):
        self.driver.find_element(By.XPATH, "//body/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[4]/a[1]").click()

    def Click_Customer_SubLink(self):
        self.driver.find_element(By.XPATH, "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p").click()

    # Add new Customer
    def Click_AddNew(self):
        self.driver.find_element(By.XPATH, "//body/div[3]/div[1]/form[1]/div[1]/div[1]/a[1]").click()

    def Enter_Email(self,Email):
        self.driver.find_element(By.ID, "Email").send_keys(Email)

    def Click_Save(self):
        self.driver.find_element(By.NAME, "save").click()

    def capture_Email(self):
        var1 = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/form[1]/section/div/div/div/div[2]/div/div[2]/div[1]/div/div/div[2]/table/tbody/tr[1]/td[2]").text
        return var1







# #Landing Page
# driver.find_element(By.XPATH, "//body/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[4]/a[1]").click()
#
# driver.find_element(By.XPATH, "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p").click()
#
#
#
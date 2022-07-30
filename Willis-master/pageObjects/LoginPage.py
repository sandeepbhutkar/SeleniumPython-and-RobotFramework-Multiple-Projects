from selenium.webdriver.common.by import By
class LoginPage:
    Txt_Email_Id = "Email"
    Txt_Password_Id = "Password"
    Btn_Login_Xpath = "//button[contains(text(),'Log in')]"

    def __init__(self,driver):
         self.driver = driver

    def Enter_Email(self, Email):
         self.driver.find_element(By.ID, self.Txt_Email_Id).clear()
         self.driver.find_element(By.ID, self.Txt_Email_Id).send_keys(Email)

    def Enter_Password(self, Password):
        self.driver.find_element(By.ID, self.Txt_Password_Id).clear()
        self.driver.find_element(By.ID, self.Txt_Password_Id).send_keys(Password)

    def Click_Login(self):
        self.driver.find_element(By.XPATH, self.Btn_Login_Xpath).click()



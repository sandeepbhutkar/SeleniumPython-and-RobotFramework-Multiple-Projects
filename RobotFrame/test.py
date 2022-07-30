from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")

driver.get("https://www.google.co.in/")
driver.maximize_window()
print(driver.title)
driver.find_element(By.XPATH,"//body/div[1]/div[3]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/input[1]").send_keys("sandeep")

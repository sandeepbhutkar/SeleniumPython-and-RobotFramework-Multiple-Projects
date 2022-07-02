from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://app.hubspot.com/login")
print(driver.title)
wait = WebDriverWait(driver, 20)
# var1 = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "form-control.private-form__control.login-email")))
# var1.send_keys("hello")

# var1 = wait.until(EC.title_is("HubSpot Login"))
# print(driver.title)

# var1 =wait.until(EC.title_contains("Hub"))
# print(driver.title)

var1 = wait.until(EC.element_to_be_clickable((By.ID, "username")))
print(driver.title)
# for class name if there are 3 class , give .(dot) in between
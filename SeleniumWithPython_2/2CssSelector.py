from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("https://www.google.com")
driver.maximize_window()
driver.find_element(By.NAME, 'q').send_keys("naveens automation")


var1 = driver.find_elements(By.CSS_SELECTOR, "ul.erkvQe li span")

print(len(var1))
#see part 1 video of Naveen for css selector

for i in var1:

    print(i.text)

    if i.text == 'naveen automation':

        i.click()
        break
driver.quit()


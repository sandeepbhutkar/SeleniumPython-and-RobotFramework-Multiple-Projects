from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
#EC variable, if we dont write EC we have to give complete expected_conditions in script.
from selenium.webdriver.support.ui import WebDriverWait

driver=webdriver.Chrome(executable_path='C:\Driver\chromedriver.exe')
driver.get('https://www.expedia.com/')
driver.find_element(By.XPATH,'//*[@id="tab-hotel-tab-hp"]/span[2]').click()
driver.find_element(By.ID,'hotel-destination-hp-hotel').clear()
driver.find_element(By.ID,'hotel-destination-hp-hotel').send_keys('DEL')
driver.find_element(By.NAME,'startDate').clear()
driver.find_element(By.NAME,'startDate').send_keys('07/04/2020')
driver.find_element(By.ID,'hotel-checkout-hp-hotel').click()
driver.find_element(By.ID,'hotel-checkout-hp-hotel').clear()
driver.find_element(By.ID,'hotel-checkout-hp-hotel').send_keys('07/04/2020')
driver.find_element(By.XPATH,"//*[@id='gcw-hotel-form-hp-hotel']/div[13]/label/button").click()

#Explicit Wait
wait=WebDriverWait(driver,60)
element=wait.until(EC.element_to_be_clickable((By.ID,"rewards-0-VIP")))
element.click()

WebDriverWait(driver,20).until(expected_condition.element=wait.until(EC.element_to_be_clickable((By.ID,"rewards-0-VIP"))))


#running scripts 3 times using while loop
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

a = 0
while (a <= 2):
    driver = webdriver.Chrome()

    driver.implicitly_wait(20)
    driver.get('https://opensource-demo.orangehrmlive.com/')
    driver.find_element_by_id("txtUsername").send_keys("Admin")
    driver.find_element_by_id("txtPassword").send_keys("admin123")
    driver.find_element_by_css_selector(".button").click()
    var1 = driver.find_element_by_xpath("//b[contains(text(),'PIM')]")
    var2 = driver.find_element_by_xpath("//a[@id='menu_pim_addEmployee']")
    var3 = ActionChains(driver)
    var3.move_to_element(var1).move_to_element(var2).click().perform()
    driver.find_element_by_id("firstName").send_keys("Sandeep")
    driver.find_element_by_id("lastName").send_keys("Bhutkar")
    var4 = driver.find_element_by_id("employeeId").get_attribute('value')
    print(var4)
    a=a+1
    driver.close()










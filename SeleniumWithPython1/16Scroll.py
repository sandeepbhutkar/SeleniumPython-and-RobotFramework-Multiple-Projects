# open browser   https://www.countries-ofthe-world.com/flags-of-the-world.html    chrome
#     maximize browser window
#     #execute javascript  window.scrollTo(0,2500)     #scroll till pixel 2500
#     #scroll element into view   xpath://*[@id="content"]/div[2]/div[2]/table[1]/tbody/tr[86]/td[1]/img     #scroll till element
#     execute javascript  window.scrollTo(0,document.body.scrollHeight)  #scroll till bottom
#     sleep  3
#     execute javascript  window.scrollTo(0,-document.body.scrollHeight)  #scroll till up

from selenium import webdriver

driver=webdriver.Chrome()

driver.get('https://www.countries-ofthe-world.com/flags-of-the-world.html')
driver.maximize_window()
#Scroll till pixel
#driver.execute_script('window.scrollTo(0,2500)')
#Scroll till element
#var1=driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[2]/table[1]/tbody/tr[86]/td[1]/img')
#driver.execute_script("arguments[0].scrollIntoView;",var1)
#scroll till end
driver.execute_script('window.scrollBy(0,document.body.scrollHeight)')
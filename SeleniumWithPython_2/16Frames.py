from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://londonfreelance.org/courses/frames/index.html")

driver.switch_to.frame("navbar")
#driver.find_element_by_css_selector("a[target='_top'][href='home.html']")
driver.find_element_by_link_text("No frames")
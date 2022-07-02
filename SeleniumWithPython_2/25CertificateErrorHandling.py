from selenium import webdriver
from selenium.webdriver.chrome.options import Options

var1 = Options()
var1.set_capability('acceptInsecureCerts', True)

driver = webdriver.Chrome(chrome_options=var1)
driver.get("https://expired.badssl.com/")      # will ignore certificate page and display website.


# there are also 2 more ways , see naveens video.
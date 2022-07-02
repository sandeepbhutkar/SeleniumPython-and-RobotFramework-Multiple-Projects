from selenium import webdriver
import unittest
import HtmlTestRunner     #pip install html-testRunner from CMD

class GoogleSearch(unittest.TestCase):        #create class
    @classmethod    #this is required to mentioned before setUpClass and tearDownClass
    def setUpClass(cls):      #create method inside class.setupClass() will run only once.setup() will run before every test method
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    def test_search_automationstepbystep(self):  #always start with test_
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Automation Step by Step")
        self.driver.find_element_by_name("q").click()
        self.driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[2]/div[2]/div[2]/center/input[1]").click()

    def test_search_sandeep(self):  #always start with test_
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("qc").send_keys("sandeep")   #deliratly given incorrect element name in order to verify Fail report.
        self.driver.find_element_by_name("q").click()
        self.driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[2]/div[2]/div[2]/center/input[1]").click()
    @classmethod
    def tearDownClass(cls):
         #tearDownwill run only once, tear down will run for all methods/functions#
        cls.driver.close()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/san/PycharmProjects/SeleniumWithPython1/HTMLReport'))
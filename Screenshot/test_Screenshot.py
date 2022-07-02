from selenium import webdriver
import logging
import pytest

class TestGoogle():
    def test_screenshot(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.google.com")
        var1 = self.driver.title
        if var1 == "Googlee":
            assert True
        else:
            self.driver.get_screenshot_as_file("C:/Users/sbhutkar/PycharmProjects/pythonProject/Screenshot/screenshot2.png")
            logging.info("TC fails check screenshot")
            assert False

        self.driver.close()



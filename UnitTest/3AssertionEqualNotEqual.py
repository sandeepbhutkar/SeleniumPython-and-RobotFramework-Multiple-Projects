import unittest
from selenium import webdriver

class Google(unittest.TestCase):
    def test_VerifyTitle1(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.google.com")
        var1 = self.driver.title
        self.assertEqual("Google", var1, "Title Matched")
        self.driver.close()

    def test_VerifyTitle2(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.google.com")
        var2 = self.driver.title
        self.assertNotEqual("Goog222le", var2, "Title Matched")
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

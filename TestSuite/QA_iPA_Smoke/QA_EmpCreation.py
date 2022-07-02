import unittest
from selenium import webdriver

class QA_Emp_Creation(unittest.TestCase):
    def test_QA_Emp_Creation1(self):
        driver = webdriver.Chrome()
        driver.get("https://www.google.com")
        var1 = driver.title
        print(var1, "QA_Emp_Creation_Checker")
    def test_QA_Emp_Creation2(self):
        print("QA_Emp_Creation_Maker")

if __name__ == "__main__":
    unittest.main()
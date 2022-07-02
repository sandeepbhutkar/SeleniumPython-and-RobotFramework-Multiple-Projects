import unittest
import HtmlTestRunner
from TestSuite.QA_iPA_Smoke.QA_EmpCreation import QA_Emp_Creation
from TestSuite.QA_iPA_Smoke.QA_MemCreation import QA_Mem_Creation

# class suite(unittest.TestCase):
#     def test_suite(self):
# Get all test
tc1 = unittest.TestLoader().loadTestsFromTestCase(QA_Emp_Creation)
tc2 = unittest.TestLoader().loadTestsFromTestCase(QA_Mem_Creation)

# create Test Suite
smoke = unittest.TestSuite([tc1,tc2])

unittest.TextTestRunner().run(smoke)
# if __name__ == "__main__":
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/sbhutkar/PycharmProjects/pythonProject/Bin"))





import unittest

class SandeepTest(unittest.TestCase):
    @unittest.SkipTest
    def test_Test1(self):
        print("Test1")
    @unittest.skip("Skip test_Test2 by specifying condition")
    def test_Test2(self):
        print("Test2")
    @unittest.skipIf(1==1, "Skipping due to some condition like driver.title==google")
    def test_Test3(self):
        print("test3")
    def test_Test4(self):
        print("test4")

if __name__ == "__name__":
    unittest.main()
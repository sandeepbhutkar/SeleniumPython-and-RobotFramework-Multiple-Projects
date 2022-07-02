import unittest

def setUpModule():
    print("Module start")     # before start of class
def tearDownModule():      #after completion of class
    print("Module End")

class SearchOperations(unittest.TestCase):

    @classmethod
    def setUp(self):         #runs before every function/method
        print("Setup")

    @classmethod
    def tearDown(self):       #runs after every function/method
        print("teardown")

    @classmethod
    def setUpClass(cls):     #runs once in class before start of function/method
        print("set up class")

    @classmethod
    def tearDownClass(cls):    #runs once in class after all function/method ends.
         print("tear down class")

    def test_search1(self):
        print("one")

    def test_search2(self):
        print("two")

    def test_search3(self):
        print("three")
if __name__ == "__main__":
    unittest.main()
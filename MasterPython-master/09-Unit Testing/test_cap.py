import unittest
import cap

class TestCap(unittest.TestCase):
    def test_one_word(self):
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result,'Python')

    def test_multiple_words(self):
        text ='learn python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Learn python')
        
# test for cap_multiple method
    def test_title_words(self):
        text = "hello how are you?"
        result = cap.cap_multiple(text)
        self.assertEqual(result,'Hello How Are You?')

if __name__ == '__main__':
    unittest.main()
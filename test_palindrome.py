import unittest
from palindrome import is_palindrome
class TestPalindrome(unittest.TestCase):
    def test_basic(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("Racecar"))
        self.assertFalse(is_palindrome("hello"))
    def test_phrases(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertTrue(is_palindrome("No lemon, no melon"))
        self.assertFalse(is_palindrome("Python is fun"))
    def test_edge_cases(self):
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome(" "))
        self.assertTrue(is_palindrome("!"))
if __name__ == "__main__":
    unittest.main()

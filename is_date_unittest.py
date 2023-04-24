import unittest
from is_date import *
# from is_date import is_leap

class TestCaseName(unittest.TestCase):
    def test_is_date(self):
        self.assertTrue(is_date("28.02.2024"))
        self.assertTrue(is_date("29.02.2004"))
        self.assertFalse(is_date("32.05.2024"))
        self.assertFalse(is_date("28.13.2025"))
    
    def test_is_leap(self):
        self.assertTrue(is_leap(2004))
        self.assertFalse(is_leap(2023))
        self.assertFalse(is_leap(2100))

    def test_type(self):
        self.assertRaises(TypeError, is_date, 3.14)

    def test_value(self):
        self.assertRaises(ValueError, is_date, "29.12")

if __name__ == '__main__':
    unittest.main()
import unittest
# from Calculating_with_Functions import *
from Calculating_with_Functions_ver2 import *


class TestFindEvenIndex(unittest.TestCase):
    def test_find_even_index(self):
        self.assertEqual(seven(times(five())), 35)
        self.assertEqual(four(plus(nine())), 13)
        self.assertEqual(eight(minus(three())), 5)
        self.assertEqual(six(divided_by(two())), 3)
        self.assertEqual(seven(divided_by(two())), 3)
    

if __name__ == '__main__':
    unittest.main()


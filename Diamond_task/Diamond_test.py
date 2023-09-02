import unittest
from Diamond import diamond
from Diamond_refactor import diamond as diamond_refactor


class TestDiamond(unittest.TestCase):
    def test_diamond(self):
        expected =  " *\n"
        expected += "***\n"
        expected += " *\n"
        self.assertEqual(diamond(1), "*\n")
        self.assertEqual(diamond(2), None)
        self.assertEqual(diamond(3), expected)
        self.assertEqual(diamond(5), "  *\n ***\n*****\n ***\n  *\n")
        self.assertEqual(diamond(7), "   *\n  ***\n *****\n*******\n *****\n  ***\n   *\n")
        self.assertEqual(diamond(0), None)
        self.assertEqual(diamond(-3), None)
    
    def test_diamond_refactor(self):
        expected =  " *\n"
        expected += "***\n"
        expected += " *\n"
        self.assertEqual(diamond_refactor(1), "*\n")
        self.assertEqual(diamond_refactor(2), None)
        self.assertEqual(diamond_refactor(3), expected)
        self.assertEqual(diamond_refactor(5), "  *\n ***\n*****\n ***\n  *\n")
        self.assertEqual(diamond_refactor(7), "   *\n  ***\n *****\n*******\n *****\n  ***\n   *\n")
        self.assertEqual(diamond_refactor(0), None)
        self.assertEqual(diamond_refactor(-3), None)

if __name__ == '__main__':
    unittest.main()

import unittest
from Hex_RGB import hex_string_to_RGB


class TestHex_string_to_RGB(unittest.TestCase):
    def test_hex_string_to_RGB(self):
        self.assertEqual(hex_string_to_RGB("#FF9933"), {'r':255, 'g':153, 'b':51})
        self.assertEqual(hex_string_to_RGB("#beaded"), {'r':190, 'g':173, 'b':237})
        self.assertEqual(hex_string_to_RGB("#000000"), {'r':0, 'g':0, 'b':0})
        self.assertEqual(hex_string_to_RGB("#111111"), {'r':17, 'g':17, 'b':17})
        self.assertEqual(hex_string_to_RGB("#Fa3456"), {'r':250, 'g':52, 'b':86})


if __name__ == '__main__':
    unittest.main()

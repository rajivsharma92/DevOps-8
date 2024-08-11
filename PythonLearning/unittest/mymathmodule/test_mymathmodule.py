import unittest

from basic import add, subtract, square_root, square, divide, multiply

class Test_mymathmodule(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1,1), 2)

    def test_subtract(self):
        self.assertEqual(subtract(2,1),1)

        self.assertEqual(subtract(1,2), -1)

    def test_square_root(self):
        self.assertEqual(square_root(4), 2)

    def test_square(self):
        self.assertEqual(square(2), 4)

    def test_multiply(self):
        self.assertEqual(multiply(2,1), 2)

    def test_divide(self):
        self.assertEqual(divide(1,1), 1)


if __name__ == '__main__':
    unittest.main()  # Added to run the tests

    
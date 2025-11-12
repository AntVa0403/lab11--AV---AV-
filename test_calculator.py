#https://github.com/AntVa0403/lab11--AV---AV-/blob/main/calculator.py
#partner 1: Anthony Vargas
#partner 2: Anthony Vargas

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    import unittest
import math
from calculator import (
    add, subtract, mul, div, logarithm, exp, hypotenuse, square_root
)

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(-2, 5), 3)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(-3, -6), 3)
        self.assertEqual(subtract(0, 5), -5)

    def test_multiply(self):
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-2, 5), -10)
        self.assertEqual(mul(0, 100), 0)

    def test_divide(self):
        self.assertAlmostEqual(div(10, 2), 5)
        self.assertAlmostEqual(div(-9, 3), -3)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(10, 0)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(2, 8), 3.0)
        self.assertAlmostEqual(logarithm(10, 1000), 3.0)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(1, 10)
        with self.assertRaises(ValueError):
            logarithm(-2, 8)
        with self.assertRaises(ValueError):
            logarithm(2, -8)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(hypotenuse(-3, 4), 5.0)

    def test_sqrt(self):
        self.assertAlmostEqual(square_root(9), 3.0)
        self.assertAlmostEqual(square_root(0), 0.0)
        with self.assertRaises(ValueError):
            square_root(-4)

if __name__ == "__main__":
    unittest.main()

import unittest
from math_function import is_even, modulo_func, is_odd, sum_function, sub_function, mul_function, div_function

class TestMathFunction(unittest.TestCase):

    def test_is_even_true(self):
        num = 4
        result = True
        self.assertEqual(is_even(num), result)

    def test_is_even_false(self):
        num = 5
        result = False
        self.assertEqual(is_even(num), result)

    def test_modulo_func(self):
        num = 5
        result = 1
        self.assertEqual(modulo_func(num), result)

    def test_is_odd_true(self):
        num = 5
        result = True
        self.assertEqual(is_odd(num), result)

    def test_is_odd_false(self):
        num = 4
        result = False
        self.assertEqual(is_odd(num), result)

    def test_sum_function_true(self):
        num_a = 5
        num_b = 5
        result = 10
        self.assertEqual(sum_function(num_a, num_b), result)

    def test_sum_function_false(self):
        num_a = 5
        num_b = 5
        result = 11
        self.assertNotEqual(sum_function(num_a, num_b), result)

    def test_sub_function_true(self):
        num_a = 5
        num_b = 5
        result = 0
        self.assertEqual(sub_function(num_a, num_b), result)

    def test_sub_function_false(self):
        num_a = 5
        num_b = 5
        result = 1
        self.assertNotEqual(sub_function(num_a, num_b), result)

    def test_mul_function_true(self):
        num_a = 5
        num_b = 5
        result = 25
        self.assertEqual(mul_function(num_a, num_b), result)

    def test_mul_function_false(self):
        num_a = 5
        num_b = 5
        result = 26
        self.assertNotEqual(mul_function(num_a, num_b), result)

    def test_div_function_true(self):
        num_a = 5
        num_b = 5
        result = 1
        self.assertEqual(div_function(num_a, num_b), result)

    def test_div_function_false(self):
        num_a = 5
        num_b = 5
        result = 0
        self.assertNotEqual(div_function(num_a, num_b), result)

if __name__ == '__main__':
    unittest.main()

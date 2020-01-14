#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def testing_max_integer(self):
        """
        testing with assetEquals the max_integer function
        self: object
        """
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([2, 4, 6, 8, 10, 12]), 12)
        self.assertEqual(max_integer([-90, 90, 90, 91]), 91)
        self.assertEqual(max_integer([-69, 69]), 69)
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([-2]), -2)
        self.assertEqual(max_integer([-2.5, -2.4]), -2.4)
        self.assertEqual(max_integer([1.1, 1.2, 1.3, 1.4]), 1.4)
        self.assertEqual(max_integer([1.1, 1.2, 1.3, float(1)]), float(1.3))
        self.assertEqual(max_integer([1.1, 1, 2.2, 2]), 2.2)
        self.assertEqual(max_integer([3/2, 1, 0.4, 1-0]), 3/2)

#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Class to test max_integer function"""

    def test_regular_input(self):
        """test for input with a list"""
        result = max_integer([10, 20, 30])
        self.assertEqual(result, 30)
        result = max_integer([10, 20, -30])
        self.assertEqual(result, 20)

    def test_sequence_type(self):
        """test for input with sequence types"""
        result = max_integer((10, 20, 30))
        self.assertEqual(result, 30)
        result = max_integer(range(1, 100))
        self.assertEqual(result, 99)
        result = max_integer([True, False])
        self.assertEqual(result, True)
        result = max_integer([(1, 2), (2, 4)])
        self.assertEqual(result, (2, 4))

    def test_sequence_element_type(self):
        """test that the elements of the sequence type are numbers"""
        with self.assertRaises(TypeError):
            max_integer((1j, 2, 3))
        with self.assertRaises(TypeError):
            max_integer(None)
        with self.assertRaises(KeyError):
            max_integer({'1': 1, '2': 2})
        

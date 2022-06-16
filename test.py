from __future__ import division
import unittest
from main import add, divide 

class TestSimpleMathOperations(unittest.TestCase):

    def test_add(self):
        _sum = add(3, 5)
        self.assertEqual(_sum, 8)
    
    def test_divide(self):
        division = divide(4, 2)
        self.assertEqual(division, float(2))
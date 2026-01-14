"""This is the test class for the math class"""
import unittest
from math1 import Math

class TestShape(unittest.TestCase):
    def setUp(self):
        self.m1 = Math(4, 5)
        self.m2 = Math(4, 2)
        self.m3 = Math(4, 0)
        
    def test_add(self):
        # check s1, s2 get_edges
        self.assertEqual(self.m1.sdd(),9)
        self.assertEqual(self.m2.sdd(),6)
        
    def test_sub(self):
        # check s1, s2 get_edges
        self.assertEqual(self.m1.sub(),-1)
        self.assertEqual(self.m2.sub(),2)
    
    def test_div(self):
        # check s1, s2 get_edges
        self.assertEqual(self.m1.mul(),20)
        self.assertEqual(self.m2.mul(),8)
        
    def test_add(self):
        # check s1, s2 get_edges
        self.assertAlmostEqual(self.m1.div(),0.8)
        self.assertAlmostEqual(self.m2.div(),2)
        self.assertEqual(self.m3.div(),None)
        
        
        
        
if __name__ == "__main__":
    unittest.main()
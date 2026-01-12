import unittest
from square import Square
 
 
class TestShape(unittest.TestCase):
 
    def setUp(self):
        self.s1 = Square(4, 4)
        self.s2 = Square(4, 4)
   
    def test_edges(self):
        # check s1, s2 get_edges
        self.assertEqual(self.s1.get_edges(), 4)
        self.assertEqual(self.s2.get_edges(), 4)
 
    def test_nodes(self):
        # check s1, s2 get_nodes
        self.assertEqual(self.s1.get_nodes(), 4)
        self.assertEqual(self.s2.get_nodes(), 4)
        
    def test_parimeter(self):
        self.assertEqual(self.s1.CalcParimeter(self.s1.set_edge_length(1)),4)
        self.assertEqual(self.s2.CalcParimeter(self.s2.set_edge_length(2)),8)
    
    def test_area(self):
        self.assertEqual(self.s1.CalcArea(self.s1.set_edge_length(1)),1)
        self.assertEqual(self.s2.CalcArea(self.s2.set_edge_length(2)),4)
   
if __name__ == "__main__":
    unittest.main()
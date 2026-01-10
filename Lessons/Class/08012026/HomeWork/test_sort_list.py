import unittest
from sortList import SortList

class TestSortList(unittest.TestCase):
    def test_sort(self):
        s1 = SortList()
        s2 = SortList()
        s3 = SortList()
        
        l1 = s1.setList()
        l2 = s2.setList()
        l3 =s3.setList()
        
        
        self.assertListEqual(s1.sortList(),sorted(l1))
        self.assertListEqual(s2.sortList(),sorted(l2))
        self.assertListEqual(s3.sortList(),sorted(l3))
 
 
if __name__ == '__main__':
    unittest.main()       
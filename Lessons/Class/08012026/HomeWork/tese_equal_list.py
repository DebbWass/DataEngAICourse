import unittest
from equalList import EqualsList

class TestEqualList(unittest.TestCase):
    def test_sort(self):
        s1 = EqualsList()
        s2 = EqualsList()
        
        
        s1.list1 = s1.setList()
        s1.list2 = s1.setList()
        
        s2.list1 = s2.list2 = s2.setList()
        
        print(s1.list1)
        print(s1.list2)
        self.assertEqual(s1.IsListsEqual(),False)
        
        print(s2.list1)
        print(s2.list2)
        self.assertEqual(s2.IsListsEqual(),True)
        
if __name__ == '__main__':
    unittest.main()       
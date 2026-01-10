import unittest
from prime import Prime

class Test_Prime(unittest.TestCase):
    def test_prime(self):
        t1 =Prime(15)
        t2 = Prime(18)
        t3 = Prime(23)
        
        self.assertFalse(t2.IsPrime())
        self.assertFalse(t1.IsPrime())
        self.assertTrue(t3.IsPrime())
        
        
if __name__ == '__main__':
    unittest.main()
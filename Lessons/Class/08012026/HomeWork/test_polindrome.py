import unittest
from polindrom import Polindrome

class Test_Polindrom(unittest.TestCase):
    def test_prime(self):
        p1 = Polindrome('123321')
        p2 = Polindrome('fndajfh')
        p3 = Polindrome('madam')
        
        self.assertTrue(p1.check_polindrome())
        self.assertFalse(p2.check_polindrome())
        self.assertTrue(p3.check_polindrome())
        
if __name__ == '__main__':
    unittest.main()
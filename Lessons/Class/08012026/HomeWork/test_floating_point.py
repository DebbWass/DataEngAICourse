import unittest
from decimal import Decimal
from floating_point_accuracy import FloatCalculator
# בהנחה והקוד הקודם נשמר בקובץ בשם float_calculator.py
# from float_calculator import FloatCalculator 

class TestFloatCalculator(unittest.TestCase):
    
    def setUp(self):
        """הכנת המחשבון לבדיקות"""
        self.calc = FloatCalculator(precision=10)

    def test_floating_point_error_exists(self):
        """בדיקה שמוכיחה שחיבור רגיל אכן מייצר שגיאת דיוק"""
        res = self.calc.standard_add(0.1, 0.2)
        # זה אמור להיות False בפייתון רגיל
        self.assertNotEqual(res, 0.3)

    def test_safe_equality(self):
        """בדיקה שמתודת ההשוואה המאובטחת שלנו עובדת"""
        sum_value = self.calc.standard_add(0.1, 0.2)
        self.assertTrue(self.calc.are_equal(sum_value, 0.3))

    def test_precise_addition(self):
        """בדיקה שחיבור Decimal מחזיר תוצאה מדויקת לחלוטין"""
        res = self.calc.precise_add(0.1, 0.2)
        self.assertEqual(res, Decimal('0.3'))

    def test_different_values(self):
        """בדיקה שהמחשבון יודע להבחין בין מספרים שבאמת שונים"""
        self.assertFalse(self.calc.are_equal(0.1 + 0.2, 0.3001))

if __name__ == '__main__':
    unittest.main()
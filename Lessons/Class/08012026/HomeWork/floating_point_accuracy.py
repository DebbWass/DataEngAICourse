import decimal
from decimal import Decimal
import math

class FloatCalculator:
    def __init__(self, precision=10):
        """
        אתחול המחשבון עם רמת דיוק רצויה להשוואות.
        """
        self.precision = precision
        self.epsilon = 10**(-precision)

    def standard_add(self, a, b):
        """חיבור רגיל (float) שמציג את חוסר הדיוק"""
        return a + b

    def precise_add(self, a, b):
        """חיבור מדויק באמצעות Decimal (מומלץ למערכות פיננסיות)"""
        # המרה למחרוזת שומרת על הדיוק המקורי שהמשתמש התכוון אליו
        return Decimal(str(a)) + Decimal(str(b))

    def are_equal(self, a, b):
        """
        בדיקת שוויון בטוחה בין שני מספרי float.
        במקום ==, בודקים אם ההפרש ביניהם קטן מאוד.
        """
        return abs(a - b) < self.epsilon

    def explain_error(self, value):
        """מחזירה את הערך כפי שהוא נשמר בזיכרון ב-50 ספרות"""
        return f"{value:.50f}"

# --- שימוש במחלקה ---

if __name__ == "__main__":
    # יצירת מופע של המחשבון
    calc = FloatCalculator(precision=15)
    
    val1 = 0.1
    val2 = 0.2
    
    # 1. חיבור רגיל
    result = calc.standard_add(val1, val2)
    print(f"Standard Addition: {val1} + {val2} = {result}")
    
    # 2. המחשת השגיאה בזיכרון
    print(f"How 0.1 actually looks in memory:\n{calc.explain_error(val1)}")
    
    # 3. בדיקת שוויון (הדרך השגויה לעומת הנכונה)
    print(f"\nSimple equality (0.1 + 0.2 == 0.3): {result == 0.3}")
    print(f"Safe equality (using Epsilon): {calc.are_equal(result, 0.3)}")
    
    # 4. שימוש ב-Decimal בתוך האובייקט
    d_result = calc.precise_add(val1, val2)
    print(f"\nPrecise (Decimal) Addition: {d_result}")
    print(f"Is Precise result exactly 0.3? {d_result == Decimal('0.3')}")
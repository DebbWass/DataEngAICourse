import unittest
from pathlib import Path
import os
from fileFinder import FileFinder
# Assuming your class is in a file named file_finder.py
# from file_finder import FileFinder 

class TestFileFinder(unittest.TestCase):
    def setUp(self):
        """
        אתחול לפני כל טסט.
        נשתמש בקובץ זמני בתיקייה שמוגדרת בקלאס שלך.
        """
        self.filename = "test.txt"
        self.finder = FileFinder(self.filename)
        
        # וידוא שהתיקייה קיימת (רק לצרכי הטסט)
        self.target_dir = self.finder.directory
        if not self.target_dir.exists():
            self.target_dir.mkdir(parents=True, exist_ok=True)

    def test_file_exists_logic(self):
        """בדיקה שהמערכת מזהה קובץ קיים ומחזירה פרטים"""
        # 1. יצירת קובץ פיזי באמת בנתיב המבוקש
        test_path = self.target_dir / self.filename
        with open(test_path, 'w') as f:
            f.write("print('test')")

        # 2. הרצת המתודות של הקלאס
        self.assertTrue(self.finder.file_exists())
        
        details = self.finder.get_file_details()
        self.assertIsNotNone(details)
        self.assertEqual(details['name'], self.filename)
        self.assertEqual(details['extension'], '.txt')


if __name__ == '__main__':
    unittest.main()
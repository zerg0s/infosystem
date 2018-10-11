from unittest import TestCase
import unittest
#from file import isPointInArea


class Test_belongingToArea(unittest.TestCase):
    def test_belongingToArea_1(self):
        isPointInArea=getattr(file, "isPointInArea")
        self.assertEqual(isPointInArea(7, 2), False)
    def test_belongingToArea_2(self):
        self.assertEqual(isPointInArea(3, 3), False) 
    def test_belongingToArea_3(self):
        self.assertEqual(isPointInArea(6, -8), True) 

if __name__ == '__main__':
    unittest.main()

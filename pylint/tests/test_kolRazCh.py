from unittest import TestCase
from kolRazCh import kolRazCh

class test_kolRazCh(TestCase):
    def test1_kolRazCh(self):
    	self.assertEqual(kolRazCh([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), 10)

    def test2_kolRazCh(self):
        self.assertEqual(kolRazCh([0, 0, 0, 0, 0, 0, 0, 0, 0]), 1)

    def test3_kolRazCh(self):
        self.assertEqual(kolRazCh([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]), 6)
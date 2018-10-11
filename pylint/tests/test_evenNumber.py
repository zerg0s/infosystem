from unittest import TestCase
from evenNumber import evenNumber

class test_evenNumber(TestCase):
    def test1_evenNumber(self):
        self.assertEqual(evenNumber([0, 2, 4, 6]), [0, 4])

    def test2_evenNumber(self):
        self.assertEqual(evenNumber([6, 3, 9, 1, 4, 6, 10]), [6, 9, 4, 10])

    def test3_evenNumber(self):
        self.assertEqual(evenNumber([1, -2, 3, -4, 5, -6]), [1, 3, 5])
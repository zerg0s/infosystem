from unittest import TestCase
from lastMax import lastMax

class test_lastMax(TestCase):
    def test1_lastMax(self):
        self.assertEqual(lastMax([1, 2, 1, 2, 1, 2]), (2, 5))

    def test2_lastMax(self):
        self.assertEqual(lastMax([5, 6, 5, 6, 5, 6]), (6, 5))

    def test3_lastMax(self):
        self.assertEqual(lastMax([6, 2, 3, 5, 6, 1]), (6, 0))
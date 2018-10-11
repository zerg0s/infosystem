from unittest import TestCase
from kolSovp import kolSovp

class test_kolSovp(TestCase):
    def test1_kolSovp(self):
        self.assertEqual(kolSovp([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]), 5)

    def test2_kolSovp(self):
        self.assertEqual(kolSovp([-1, 1, -1], [-2, 2, -2]), 4)

    def test3_kolSovp(self):
        self.assertEqual(kolSovp([0, 0, 0], [0, 0, 0]), 1)
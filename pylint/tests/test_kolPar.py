from unittest import TestCase
from kolPar import kolPar

class test_kolPar(TestCase):
    def test1_kolPar(self):
        self.assertEqual(kolPar([1, 2, 3, 4, 5]), 0)

    def test2_kolPar(self):
        self.assertEqual(kolPar([1, 1, 1, 0, 1]), 6)

    def test3_kolPar(self):
        self.assertEqual(kolPar([1, 1, 1, 1, 1, 1]), 15)
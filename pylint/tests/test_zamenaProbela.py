from unittest import TestCase
from zamenaProbela import zamenaProbela

class test_zamenaProbela(TestCase):
    def test1_zamenaProbela(self):
        self.assertEqual(zamenaProbela("t e s t"), "t*e*s*t")

    def test2_zamenaProbela(self):
        self.assertEqual(zamenaProbela("1      2      3"), "1*2*3")

    def test3_zamenaProbela(self):
        self.assertEqual(zamenaProbela("1   2   3   4   5   6"), "1*2*3*4*5*6")
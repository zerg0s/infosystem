from unittest import TestCase
from evklid import gcd

class test_evklid(TestCase):
    def test1_evklid(self):
        self.assertEqual(gcd(1, 1), 1)

    def test2_evklid(self):
        self.assertEqual(gcd(520, 56), 8)

    def test3_evklid(self):
        self.assertEqual(gcd(130, 130), 130)
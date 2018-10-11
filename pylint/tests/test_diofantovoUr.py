from unittest import TestCase
from diofantovoUr import diofantovoUr

class test_diofantovoUr(TestCase):
    def test1_diofantovoUr(self):
        self.assertEqual(diofantovoUr(1, 0, 1, 4, 1), 0)

    def test2_diofantovoUr(self):
        self.assertEqual(diofantovoUr(1, 1, 1, 1, 1), 0)

    def test3_diofantovoUr(self):
        self.assertEqual(diofantovoUr(0, 0, 0, 3, 0), 0)
from unittest import TestCase
from test1 import test1

class test_test1(TestCase):
    def test1_test1(self):
        self.assertEqual(test1(17), "Ошибка! Введено неверное число!")

    def test2_test1(self):
        self.assertEqual(test1(16), 2)

    def test3_test1(self):
        self.assertEqual(test1(15), 4)
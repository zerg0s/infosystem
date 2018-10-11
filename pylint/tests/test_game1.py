from unittest import TestCase
from game1 import game1

class test_game1(TestCase):
    def test1_game1(self):
        self.assertEqual(game1(9, -1, 2, 3), "Неверно введены числа. Попробуйте еще раз!")

    def test2_game1(self):
        self.assertEqual(game1(6, 3, 4, 8), "NO!")

    def test3_game1(self):
        self.assertEqual(game1(4, 4, 5, 5), "YES!")
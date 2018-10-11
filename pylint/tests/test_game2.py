from unittest import TestCase
from game2 import game2

class test_game2(TestCase):
    def test1_game2(self):
        self.assertEqual(game2(-52, 6, 2, 1), "Неверно введены числа. Попробуйте еще раз!")

    def test2_game2(self):
        self.assertEqual(game2(6, 5, 2, 1), "NO!")

    def test3_game2(self):
        self.assertEqual(game2(6, 4, 5, 4), "YES!")
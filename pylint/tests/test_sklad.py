from unittest import TestCase
from sklad import sklad

class test_sklad(TestCase):
    def test1_sklad(self):
        self.assertEqual("Ошибка! Число должно быть больше 1!", sklad(0, 1, 2, 3, 4, 5))

    def test2_sklad(self):
        self.assertEqual(sklad(100, 200, 300, 400, 500, 600), 0.0)

    def test3_sklad(self):
        self.assertEqual(sklad(50, 100, 150, 156, 157, 158), 0.0)
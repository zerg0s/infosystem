from unittest import TestCase
from peresadki import peresadki

class test_peresadki(TestCase):
    def test1_peresadki(self):
        self.assertEqual(peresadki(101, 1, 1, 1), "Ошибка! Число больше 100 вводить нельзя!")

    def test2_peresadki(self):
        self.assertEqual(peresadki(4, 2, 7, 9), 0)

    def test3_peresadki(self):
        self.assertEqual(peresadki(1, 6, 2, 8), 5)
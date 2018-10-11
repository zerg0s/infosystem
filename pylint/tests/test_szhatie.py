from unittest import TestCase
from szhatie import szhatie

class test_szhatie(TestCase):
    def test1_szhatie(self):
        self.assertEqual(szhatie([0, 0, 0, 0, 1, 2, 3, 4]), [1, 2, 3, 4, 0, 0, 0, 0])

    def test2_szhatie(self):
        self.assertEqual(szhatie([0, 0, 1, 0, 0, 0, 0, 1]), [1, 1, 0, 0, 0, 0, 0, 0])

    def test3_szhatie(self):
        self.assertEqual(szhatie([5, 32, 0, 55, 16, 1, 0, 25, 0]), [5, 32, 55, 16, 1, 25, 0, 0, 0])
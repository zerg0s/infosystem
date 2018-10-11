from unittest import TestCase
from third import third

class test_third(TestCase):
    def test1_third(self):
        self.assertEqual(third("test"), "es")

    def test2_third(self):
        self.assertEqual(third("qweqwe"), "wewe")

    def test3_third(self):
        self.assertEqual(third("1 2 3 4 5"), " 23  5")
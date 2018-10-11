from unittest import TestCase
from inversion import inversion

class test_inversion(TestCase):
    def test1_inversion(self):
        self.assertEqual(inversion("test string"), "string test")

    def test2_inversion(self):
        self.assertEqual(inversion("245 abc"), "abc 245")

    def test3_inversion(self):
        self.assertEqual(inversion("egebefb sgrrwgeg"), "sgrrwgeg egebefb")
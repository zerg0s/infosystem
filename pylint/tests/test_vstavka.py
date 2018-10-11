from unittest import TestCase
from vstavka import vstavka

class test_vstavka(TestCase):
    def test1_vstavka(self):
        self.assertEqual(vstavka("123"), "1*2*3")

    def test2_vstavka(self):
        self.assertEqual(vstavka("stroka"), "s*t*r*o*k*a")

    def test3_vstavka(self):
        self.assertEqual(vstavka("321"), "3*2*1")
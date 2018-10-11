from unittest import TestCase
from run import run

class test_run(TestCase):
    def test1_run(self):
        self.assertEqual(run(0, 30), "Ошибка! В 1-ый день спортсмен не может пробежать 0 км!")

    def test2_run(self):
        self.assertEqual(run(10, 20), 9)

    def test3_run(self):
        self.assertEqual(run(23, 37), 6)
	def test3_run(self):
		self.assertEqual(run(23, 3333), 6)
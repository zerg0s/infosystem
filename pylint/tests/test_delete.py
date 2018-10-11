from unittest import TestCase
from delete import delete

class test_delete(TestCase):
    def test1_delete(self):
        self.assertEqual(delete("de@l@ete@"), "delete")

    def test2_delete(self):
        self.assertEqual(delete("r@u@n@"), "run")

    def test3_delete(self):
        self.assertEqual(delete("@121@31@4@"), "121314")
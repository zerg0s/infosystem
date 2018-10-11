from unittest import TestCase
from fragments import fragments

class test_fragments(TestCase):
    def test1_fragments(self):
        self.assertEqual(fragments("1h1h1h1h1h1h"), "1h1H1H1H1H1h")

    def test2_fragments(self):
        self.assertEqual(fragments("jhfuhdlfhtkvhelfh"), "jhfuHdlfHtkvHelfh")

    def test3_fragments(self): 
        self.assertEqual(fragments("24h1111h11231h"), "24h1111H11231h")
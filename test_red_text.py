from unittest import TestCase
from game import red_text


class TestRedText(TestCase):
    def test_red_text(self):
        expected = "\x1b[1;31;40mhello\x1b[0m"
        actual = red_text("hello")
        self.assertEqual(expected, actual)

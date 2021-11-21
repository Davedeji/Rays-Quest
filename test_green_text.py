from unittest import TestCase
from game import green_text


class TestGreenText(TestCase):
    def test_green_text(self):
        expected = "\x1b[1;32;40mhello\x1b[0m"
        actual = green_text("hello")
        self.assertEqual(expected, actual)

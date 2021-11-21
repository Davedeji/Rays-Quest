from unittest import TestCase
from unittest.mock import patch
import io
from game import character_flees


class TestCharacterFlees(TestCase):
    def test_character_flees(self):
        test_character = {}
        test_foe = {}
        character_flees(test_character, test_foe)



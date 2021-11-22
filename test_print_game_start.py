from unittest import TestCase
from unittest.mock import patch
import io
from game import print_game_start


class TestPrintGameStart(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_game_start(self, mock_stdout):
        expected = """So boom, You're awoken by the sound of loud thunders.
You have 10hp.
Your goal is to get to the north east end of the map and defeat the boss.
Follow the prompts provided by the game to get started.
You can enter 'q' at any point to quit the game
Bon Voyage!!
🚹 - Your character
🈵 - Walls
⚠️ - Final Boss
"""
        print_game_start()
        self.assertEqual(expected, mock_stdout.getvalue())

from unittest import TestCase
from unittest.mock import patch
import io
import game


class TestGetDirectionChoice(TestCase):
    @patch('game.check_quit', return_value='w')
    @patch('builtins.input', side_effect=['b', 'w'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_direction_choice_incorrect_correct(self, mock_stdout, _, __):
        expected_print = """list of directions:
w Up
d Right
a Left
s Down
"""
        expected_choice = 'w'
        actual_choice = game.get_direction_choice()
        self.assertEqual(expected_choice, actual_choice)
        self.assertEqual(expected_print, mock_stdout.getvalue())

    @patch('game.check_quit', return_value='a')
    @patch('builtins.input', side_effect=['a'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_direction_choice_correct(self, mock_stdout, _, __):
        expected_print = """list of directions:
w Up
d Right
a Left
s Down
"""
        expected_choice = 'a'
        actual_choice = game.get_direction_choice()
        self.assertEqual(expected_choice, actual_choice)
        self.assertEqual(expected_print, mock_stdout.getvalue())

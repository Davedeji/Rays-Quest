from unittest import TestCase
from unittest.mock import patch
import io
import game


class TestValidateNumChoice(TestCase):
    @patch('game.check_quit', side_effect=['b', '3'])
    @patch('builtins.input', side_effect=['b', '3'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_validate_num_choice_incorrect_correct(self, mock_stdout, _, __):
        expected_print = "\x1b[1;31;40mInvalid Choice\x1b[0m\n"
        expected_choice = '3'
        actual_choice = game.validate_num_choice("Enter choice", 5)
        self.assertEqual(expected_choice, actual_choice)
        self.assertEqual(expected_print, mock_stdout.getvalue())

    @patch('game.check_quit', return_value='3')
    @patch('builtins.input', side_effect=['3'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_validate_num_choice_correct(self, mock_stdout, _, __):
        expected_print = ""
        expected_choice = '3'
        actual_choice = game.validate_num_choice("Enter choice", 5)
        self.assertEqual(expected_choice, actual_choice)
        self.assertEqual(expected_print, mock_stdout.getvalue())

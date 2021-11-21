from unittest import TestCase
from unittest.mock import patch
import io
from game import check_quit


class TestCheckQuit(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_quit_true(self, mock_stdout):
        expected = "\nGoodbye!\n"
        self.assertRaises(SystemExit, check_quit, 'q')
        self.assertEqual(expected, mock_stdout.getvalue())

    def test_check_quit_false(self):
        expected = '3'
        actual = check_quit('3')
        self.assertEqual(expected, actual)

from unittest import TestCase
from unittest.mock import patch
import io
from game import describe_current_location


class TestDescribeCurrentLocation(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location(self, mock_stdout):
        character = {"X-coordinate": 0, "Y-coordinate": 0}
        expected = "Your Coordinates are:\nX: 0 Y: 0\n\n"
        describe_current_location(character)
        self.assertEqual(expected, mock_stdout.getvalue())

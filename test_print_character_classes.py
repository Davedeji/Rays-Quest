from unittest import TestCase
from unittest.mock import patch
import io
from game import print_character_classes


class TestPrintCharacterClasses(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_classes(self, mock_stdout):
        expected = """
These are the available classes:
1 INSTIGATOR : Loves chaos, uses whatever tools at their disposal.
2 LURKER : Slips into the background, Decent at everything.
3 PROTECTOR : The guardians! most resistant to attacks
4 DISTRIBUTOR : Most accurate of the bunch.
"""
        print_character_classes()
        self.assertEqual(mock_stdout.getvalue(), expected)


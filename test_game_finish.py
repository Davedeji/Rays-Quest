from unittest import TestCase
from unittest.mock import patch
import io
from game import game_finish


class TestGameFinish(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_game_finish_win(self, mock_stdout):
        expected = """
        
                                         .''.
               .''.             *''*    :_\/_:     .
              :_\/_:   .    .:.*_\/_*   : /\ :  .'.:.'.
          .''.: /\ : _\(/_  ':'* /\ *  : '..'.  -=:o:=-
         :_\/_:'.:::. /)\*''*  .|.* '.'/.'_\(/_'.':'.'
         : /\ : :::::  '*_\/_* | |  -= o =- /)\    '  *
          '..'  ':::'   * /\ * |'|  .'/.'.  '._____
              *        __*..* |  |     :      |.   |' .---"|
               _*   .-'   '-. |  |     .--'|  ||   | _|    |
            .-'|  _.|  |    ||   '-__  |   |  |    ||      |
            |' | |.    |    ||       | |   |  |    ||      |
         ___|  '-'     '    ""       '-'   '-.'    '`      |____
        jgs~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        
        ------------------------------------------------
        
        
"""
        game_finish(True)
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_game_finish_loose(self, mock_stdout):
        expected = "You lost. Better luck next time\n"
        game_finish(False)
        self.assertEqual(expected, mock_stdout.getvalue())
import unittest
import classes

class TestGameBoardMethods(unittest.TestCase):

    def setUp(self):
        self.game_board = classes.GameBoard()
        self.game_board.generate_board()

    def test_game_board_class_exists(self):
        self.assertIsNotNone(self.game_board)

    def test_game_board_has_board_property(self):
        self.assertIsNotNone(self.game_board.board)

    def test_game_board_is_list(self):
        self.assertTrue(type(self.game_board.board) is list)
    
    def test_game_board_is_list_of_lists(self):
        for row in self.game_board.board:
            self.assertTrue(type(row) is list)
    
    def test_game_board_rows_are_not_blank(self):
        for row in self.game_board.board:
            self.assertTrue(len(row))

    def test_each_game_row_has_four_numbers(self):
        for row in self.game_board.board:
            self.assertTrue(len(row) == 4)

if __name__ == '__main__':
    unittest.main(verbosity=2)
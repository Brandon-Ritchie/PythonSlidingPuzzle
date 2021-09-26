import unittest
import classes

class TestGameMethods(unittest.TestCase):

    def setUp(self):
        pieces = classes.generate_pieces()
        board = classes.generate_board(pieces)
        self.game = classes.Game(board)
        self.game.create_piece_dictionary(pieces)
        self.game_piece = classes.GamePiece(2, (2,3))

    def test_game_class_exists(self):
        self.assertIsNotNone(self.game)

    def test_game_has_board_property(self):
        self.assertIsNotNone(self.game.board)
    
    def test_game_board_is_list_of_lists(self):
        for row in self.game.board:
            self.assertTrue(type(row) is list)
    
    def test_game_board_rows_are_not_blank(self):
        for row in self.game.board:
            self.assertTrue(len(row))

    def test_each_game_row_has_four_game_pieces(self):
        for row in self.game.board:
            self.assertTrue(len(row) == 4)

    def test_game_piece_class_exists(self):
        self.assertIsNotNone(self.game_piece)

    def test_game_piece_position_returns_tuple(self):
        self.assertEqual(self.game_piece.position, (2, 3))
    
    def test_game_has_piece_dict(self):
        self.assertIsNotNone(self.game._piece_dictionary)
    
    def test_game_piece_dictionary_is_dict(self):
        self.assertTrue(type(self.game.piece_dictionary) is dict)

    def test_game_piece_dictionary_has_1_to_15(self):
        for i in range(1, 16):
            self.assertIn(i, self.game.piece_dictionary)
    

if __name__ == '__main__':
    unittest.main(verbosity=2)
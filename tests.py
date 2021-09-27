import unittest
import classes
from main import generate_pieces, generate_board

class TestGameMethods(unittest.TestCase):

    def setUp(self):
        pieces = generate_pieces()
        board = generate_board(pieces)
        self.game = classes.Game(board)
        self.game.create_piece_dictionary(pieces)
        self.game_piece = classes.GamePiece(2, (1, 1))
        self.above_open_game_piece = classes.GamePiece(' ', (0, 1))
        self.below_open_game_piece = classes.GamePiece(' ', (2, 1))
        self.left_open_game_piece = classes.GamePiece(' ', (1, 0))
        self.right_open_game_piece = classes.GamePiece(' ', (1, 2))
        self.distant_open_game_piece = classes.GamePiece(' ', (3, 3))

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
        self.assertEqual(self.game_piece.position, (1, 1))
    
    def test_game_has_piece_dict(self):
        self.assertIsNotNone(self.game._piece_dictionary)
    
    def test_game_piece_dictionary_is_dict(self):
        self.assertTrue(type(self.game.piece_dictionary) is dict)

    def test_game_piece_dictionary_has_1_to_15(self):
        for i in range(1, 16):
            self.assertIn(i, self.game.piece_dictionary)
    
    def test_game_piece_above_open(self):
        move_piece_return = self.game.move_piece(self.game_piece, self.above_open_game_piece)
        self.assertEqual(move_piece_return, 'Open space is above')

    def test_open_game_piece_is_below(self):
        move_piece_return = self.game.move_piece(self.game_piece, self.below_open_game_piece)
        self.assertEqual(move_piece_return, 'Open space is below')
    
    def test_open_game_piece_is_left(self):
        move_piece_return = self.game.move_piece(self.game_piece, self.left_open_game_piece)
        self.assertEqual(move_piece_return, 'Open space is to the left')

    def test_open_game_piece_is_right(self):
        move_piece_return = self.game.move_piece(self.game_piece, self.right_open_game_piece)
        self.assertEqual(move_piece_return, 'Open space is to the right')
    
    def test_open_game_piece_too_far(self):
        move_piece_return = self.game.move_piece(self.game_piece, self.distant_open_game_piece)
        self.assertEqual(move_piece_return, 'Piece is not next to open space')

if __name__ == '__main__':
    unittest.main(verbosity=2)
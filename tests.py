import unittest
import classes
from main import generate_pieces

class TestGameMethods(unittest.TestCase):

    def setUp(self):
        pieces = generate_pieces()
        self.pieces = pieces
        self.game = classes.Game()
        self.game.generate_board(pieces)
        self.game.create_piece_dictionary(pieces)
        self.game_piece = classes.GamePiece(2, (1, 1))
        self.game_piece_above = classes.GamePiece(2, (2, 3))
        self.game_piece_left = classes.GamePiece(2, (3, 2))

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

    def test_open_game_piece_is_below(self):
        move_piece_return = self.game.find_open_space_direction(self.game_piece_above)
        self.assertEqual(move_piece_return, 'Below')

    def test_open_game_piece_is_right(self):
        move_piece_return = self.game.find_open_space_direction(self.game_piece_left)
        self.assertEqual(move_piece_return, 'Right')
    
    def test_open_game_piece_too_far(self):
        move_piece_return = self.game.find_open_space_direction(self.game_piece)
        self.assertEqual(move_piece_return, 'Too Far')
    
    def test_move_piece_open_piece_is_below(self):
        returned_value = True
        try:
            self.game.move_piece(self.game_piece_above)
        except:
            returned_value = False
        self.assertTrue(returned_value)
    
    def test_move_piece_open_piece_is_right(self):
        returned_value = True
        try:
            self.game.move_piece(self.game_piece_left)
        except:
            returned_value = False
        self.assertTrue(returned_value)

    def test_move_piece_too_far(self):
        returned_value = True
        try:
            self.game.move_piece(self.game_piece)
        except:
            returned_value = False
        self.assertTrue(returned_value)
    
    def test_puzzle_is_not_completed(self):
        self.assertFalse(self.game.is_puzzle_completed(self.game.board))

    def test_puzzle_is_completed(self):
        self.game.board = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, ' ']]
        self.assertTrue(self.game.is_puzzle_completed(self.game.board))
        
if __name__ == '__main__':
    unittest.main(verbosity=2)
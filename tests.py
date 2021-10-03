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
        self.test_piece = classes.GamePiece(2, (1, 1))

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
        self.assertIsNotNone(self.test_piece)

    def test_game_piece_position_returns_tuple(self):
        self.assertEqual(self.test_piece.position, (1, 1))
    
    def test_game_has_piece_dict(self):
        self.assertIsNotNone(self.game._piece_dictionary)
    
    def test_game_piece_dictionary_is_dict(self):
        self.assertTrue(type(self.game.piece_dictionary) is dict)

    def test_game_piece_dictionary_has_1_to_15(self):
        for i in range(1, 16):
            self.assertIn(i, self.game.piece_dictionary)
    
    def test_move_piece_open_piece_is_below(self):
        self.game.piece_dictionary[' '] = (2, 1)
        self.game.piece_dictionary[self.test_piece.num] = self.test_piece.position
        returned_value = self.game.move_piece(self.test_piece)
        self.assertTrue(returned_value)
    
    def test_move_piece_open_piece_is_above(self):
        self.game.piece_dictionary[' '] = (0, 1)
        self.game.piece_dictionary[self.test_piece.num] = self.test_piece.position
        returned_value = self.game.move_piece(self.test_piece)
        self.assertTrue(returned_value)
    
    def test_move_piece_open_piece_is_right(self):
        self.game.piece_dictionary[' '] = (1, 2)
        self.game.piece_dictionary[self.test_piece.num] = self.test_piece.position
        returned_value = self.game.move_piece(self.test_piece)
        self.assertTrue(returned_value)

    def test_move_piece_open_piece_is_left(self):
        self.game.piece_dictionary[' '] = (1, 0)
        self.game.piece_dictionary[self.test_piece.num] = self.test_piece.position
        returned_value = self.game.move_piece(self.test_piece)
        self.assertTrue(returned_value)
    
    def test_move_piece_open_piece_is_above_left_diagonal(self):
        self.game.piece_dictionary[' '] = (0, 0)
        self.game.piece_dictionary[self.test_piece.num] = self.test_piece.position
        returned_value = self.game.move_piece(self.test_piece)
        self.assertFalse(returned_value)
    
    def test_move_piece_open_piece_is_above_right_diagonal(self):
        self.game.piece_dictionary[' '] = (0, 2)
        self.game.piece_dictionary[self.test_piece.num] = self.test_piece.position
        returned_value = self.game.move_piece(self.test_piece)
        self.assertFalse(returned_value)

    def test_move_piece_open_piece_is_below_left_diagonal(self):
        self.game.piece_dictionary[' '] = (2, 0)
        self.game.piece_dictionary[self.test_piece.num] = self.test_piece.position
        returned_value = self.game.move_piece(self.test_piece)
        self.assertFalse(returned_value)

    def test_move_piece_open_piece_is_below_right_diagonal(self):
        self.game.piece_dictionary[' '] = (2, 2)
        self.game.piece_dictionary[self.test_piece.num] = self.test_piece.position
        returned_value = self.game.move_piece(self.test_piece)
        self.assertFalse(returned_value)

    def test_move_piece_too_far(self):
        self.game.piece_dictionary[self.test_piece.num] = self.test_piece.position
        returned_value = self.game.move_piece(self.test_piece)
        self.assertFalse(returned_value)
    
    def test_puzzle_is_not_completed(self):
        self.assertFalse(self.game.is_puzzle_completed())

    def test_puzzle_is_completed(self):
        self.game.piece_dictionary[1] = (0, 0)
        self.game.piece_dictionary[2] = (0, 1)
        self.game.piece_dictionary[3] = (0, 2)
        self.game.piece_dictionary[4] = (0, 3)
        self.game.piece_dictionary[5] = (1, 0)
        self.game.piece_dictionary[6] = (1, 1)
        self.game.piece_dictionary[7] = (1, 2)
        self.game.piece_dictionary[8] = (1, 3)
        self.game.piece_dictionary[9] = (2, 0)
        self.game.piece_dictionary[10] = (2, 1)
        self.game.piece_dictionary[11] = (2, 2)
        self.game.piece_dictionary[12] = (2, 3)
        self.game.piece_dictionary[13] = (3, 0)
        self.game.piece_dictionary[14] = (3, 1)
        self.game.piece_dictionary[15] = (3, 2)
        self.game.piece_dictionary[' '] = (3, 3)

        self.assertTrue(self.game.is_puzzle_completed())

    def test_can_piece_move_function_exists(self):
        returned_value = True
        try:
            self.game.can_piece_move(self.test_piece)
        except:
            returned_value = False
        self.assertTrue(returned_value)

if __name__ == '__main__':
    unittest.main(verbosity=2)
class Game():

    def __init__(self, board):
        self._board = board

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, board):
        self._board = board

    @property
    def piece_dictionary(self):
        return self._piece_dictionary
    
    @piece_dictionary.setter
    def piece_dictionary(self, dict_of_pieces):
        if type(dict_of_pieces) is dict:
            self._piece_dictionary = dict_of_pieces
    
    def create_piece_dictionary(self, pieces):
        self.piece_dictionary = {}
        for piece in pieces:
            self.piece_dictionary[piece.num] = piece.position

    def find_open_space_direction(self, piece):
        open_space_position = self.piece_dictionary[' ']
        if piece.position[0] == open_space_position[0]:
            if piece.position[1] -1 == open_space_position[1]:
                return 'Left'
            elif piece.position[1] + 1 == open_space_position[1]:
                return 'Right'
        elif piece.position[1] == open_space_position[1]:
            if piece.position[0] - 1 == open_space_position[0]:
                return 'Above'
            elif piece.position[0] + 1 == open_space_position[0]:
                return 'Below'
        else:
            return 'Too Far'

    def move_piece(self, piece):
        open_space_direction = self.find_open_space_direction(piece)
        if open_space_direction != 'Too Far':
            temp_open_space_position = self.piece_dictionary[' ']
            self.piece_dictionary[' '] = piece.position
            self.piece_dictionary[piece] = temp_open_space_position
            self.update_board()
        
    def update_board(self):
        for key, value in self.piece_dictionary.items():
            piece_row_value = value[0]
            piece_column_value = value[1]
            self.board[piece_row_value][piece_column_value] = key

class GamePiece():

    def __init__(self, num, position):
        self._num = num
        self._position = position

    def __repr__(self):
        return str(self._num)

    @property
    def num(self):
        return self._num
    
    @num.setter
    def num(self, number):
        if type(number) is int:
            self._num = number
    
    @property
    def position(self):
        return self._position
    
    @position.setter
    def position(self, tup):
        if type(tup) is tuple:
            self._position
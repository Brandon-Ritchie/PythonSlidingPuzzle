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

    def move_piece(self, piece, open_piece):
        piece_position = piece.position
        open_space_position = open_piece.position
        if piece_position[0] == open_space_position[0]:
            if piece_position[1] -1 == open_space_position[1]:
                return 'Open space is to the left'
            elif piece_position[1] + 1 == open_space_position[1]:
                return 'Open space is to the right'
        elif piece_position[1] == open_space_position[1]:
            if piece_position[0] - 1 == open_space_position[0]:
                return 'Open space is above'
            elif piece_position[0] + 1 == open_space_position[0]:
                return 'Open space is below'
        else:
            return 'Piece is not next to open space'



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
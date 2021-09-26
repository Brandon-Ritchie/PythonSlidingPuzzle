import random

def generate_list_of_num():
    list_of_num = []
    
    while len(list_of_num) < 15:
        random_num = random.randint(1, 15)
        if random_num not in list_of_num:
            list_of_num.append(random_num)
        
    return list_of_num

def generate_pieces():
    list_of_num_for_pieces = generate_list_of_num()

    pieces = []

    for i in range(0,4):
        for j in range(0, 4):
            if len(list_of_num_for_pieces) == 0:
                pieces.append(GamePiece(' ', (i, j)))
            else:
                pieces.append(GamePiece(list_of_num_for_pieces[0], (i, j)))
                list_of_num_for_pieces.pop(0)

    return pieces

def generate_board(pieces):

    list_of_pieces = []

    for piece in pieces:
        list_of_pieces.append(piece)

    board = [[], [], [], []]

    for i in range(0,4):
        for j in range(0, 4):
            if len(list_of_pieces) == 0:
                break
            else:
                board[i].append(list_of_pieces[0])
                list_of_pieces.pop(0)
    
    return board

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

    def move_piece(self, piece):
        pass

    

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
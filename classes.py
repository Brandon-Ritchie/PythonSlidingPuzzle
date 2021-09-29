class Game():

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
        piece_position = self.piece_dictionary[piece.num]
        if piece_position[0] == open_space_position[0]:
            if piece_position[1] -1 == open_space_position[1]:
                return 'Left'
            elif piece_position[1] + 1 == open_space_position[1]:
                return 'Right'
        elif piece_position[1] == open_space_position[1]:
            if piece_position[0] - 1 == open_space_position[0]:
                return 'Above'
            elif piece_position[0] + 1 == open_space_position[0]:
                return 'Below'
        else:
            return 'Too Far'

    def move_piece(self, piece):
        open_space_direction = self.find_open_space_direction(piece)
        temp_open_space_position = self.piece_dictionary[' ']
        piece_position = self.piece_dictionary[piece.num]
        if open_space_direction != 'Too Far':
            self.piece_dictionary[' '] = piece_position
            self.piece_dictionary[piece.num] = temp_open_space_position
        else:
            print('That piece is not next to the open space. Please choose a different piece.')
    
    def generate_board(self, pieces):

        list_of_pieces = []

        for piece in pieces:
            list_of_pieces.append(piece)

        self.board = [[], [], [], []]

        for i in range(0,4):
            for j in range(0, 4):
                if len(list_of_pieces) == 0:
                    break
                else:
                    self.board[i].append(list_of_pieces[0])
                    list_of_pieces.pop(0)

    def update_board(self, pieces):

        for key, value in self.piece_dictionary.items():
            for piece in pieces:
                if piece.num == key:
                    (row, column) = value
                    piece.position = value
                    self.board[row][column] = piece
        
        for row in self.board:
            print(row)

    def is_puzzle_completed(self, board):
        completed_puzzle_list = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, ' ']]

        if board == completed_puzzle_list:
            return True
        else:
            return False

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
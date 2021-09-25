import random

class GameBoard():

    @property
    def board(self):
        return self._board
    
    def generate_board(self):
    
        self._board = [[], [], [], []]

        list_of_num_for_pieces = []
    
        while len(list_of_num_for_pieces) < 15:
            random_num = random.randint(1, 15)
            if random_num not in list_of_num_for_pieces:
                list_of_num_for_pieces.append(random_num)

        for i in range(0,4):
            for j in range(0, 4):
                if len(list_of_num_for_pieces) == 0:
                    self.board[i].append(' ')
                else:
                    self.board[i].append(list_of_num_for_pieces[0])
                    list_of_num_for_pieces.pop(0)

class GamePiece():

    def __init__(self, num, can_move):
        self._num = num
        self._can_move = can_move

    def __repr__(self):
        return self._num

    @property
    def num(self):
        return self._num
    
    @num.setter
    def num(self, number):
        if type(number) is int:
            self._num = number
    
    @property
    def can_move(self):
        return self._can_move
    
    @can_move.setter
    def can_move(self, boolean):
        if type(boolean) is bool:
            self._can_move = boolean
    
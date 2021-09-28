import classes
import random

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
                pieces.append(classes.GamePiece(' ', (i, j)))
            else:
                pieces.append(classes.GamePiece(list_of_num_for_pieces[0], (i, j)))
                list_of_num_for_pieces.pop(0)

    return pieces

if __name__ == '__main__':
    pieces = generate_pieces()
    board = generate_board(pieces)
    game = classes.Game(board)
    game.create_piece_dictionary(pieces)
    game.update_board()
    for row in game.board:
        print(row)
import classes

if __name__ == '__main__':
    pieces = classes.generate_pieces()
    board = classes.generate_board(pieces)
    game = classes.Game(board)
    game.create_piece_dictionary(pieces)
    print(game.piece_dictionary)
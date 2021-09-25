import classes

if __name__ == '__main__':
    game_board = classes.GameBoard()
    game_board.generate_board()
    for item in game_board.board:
        print(item)
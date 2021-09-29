from typing import ValuesView
import classes
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
                pieces.append(classes.GamePiece(' ', (i, j)))
            else:
                pieces.append(classes.GamePiece(list_of_num_for_pieces[0], (i, j)))
                list_of_num_for_pieces.pop(0)

    return pieces

if __name__ == '__main__':
    try:
        pieces = generate_pieces()
        game = classes.Game()
        game.generate_board(pieces)
        game.create_piece_dictionary(pieces)

        valid_rows_and_columns = [1, 2, 3, 4]

        puzzle_completed = False
        
        for row in game.board:
                print(row)

        while puzzle_completed is False:

            print('Choose the row of the piece you want to move:')
            chosen_row = input()
            
            print('Choose the column of the piece you want to move:')
            chosen_column = input()
            

            try:
                chosen_piece = game.board[int(chosen_row) - 1][int(chosen_column) - 1]

                game.move_piece(chosen_piece)

                game.update_board(pieces)

                if game.is_puzzle_completed(game.board) == True:
                    puzzle_completed = True
            except:
                print('Invalid move. Please enter numbers between 1 and 4!')
                
                for row in game.board:
                    print(row)
        
        print('You have completed the puzzle!!')

    except KeyboardInterrupt:
        exit()
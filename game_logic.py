
def logic(board, row, col, gamer):

    choice = row
    if (gamer == 1):
        change = 'X'
    else:
        change = 'O'
    if (choice == 0):

        if(col == 1 and board[0] == 0):
            index = 0
            board[0] = change
            return index
        elif(col == 2 and board[1] == 1):
            index = 1
            board[1] = change
            return index

        elif(col == 3 and board[2] == 2):
            index = 2
            board[2] = change
            return index

    if(choice == 1):
        if(col == 1 and board[3] == 3):
            index = 3
            board[3] = change
            return index

        elif(col == 2 and board[4] == 4):
            index = 4
            board[4] = change
            return index

        elif(col == 3 and board[5] == 5):
            index = 5
            board[5] = change
            return index

    if(choice == 2):
        if(col == 1 and board[6] == 6):
            index = 6
            board[6] = change
            return index

        elif(col == 2 and board[7] == 7):
            index = 7
            board[7] = change
            return index

        elif(col == 3 and board[8] == 8):
            index = 8
            board[8] = change
            return index
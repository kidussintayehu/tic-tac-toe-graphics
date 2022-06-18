from constants import *
from draw_win_line import *

def checkWin(board, player):
    """
    It checks if the player has won the game by checking if there are three of the same player's pieces
    in a row, column, or diagonal.
    
    :param board: the board to check for a win
    :param player: the player who won
    :return: a boolean value.
    """
    # vertical win
    for col in range(BOARD_COLS):
        if (board[col] == board[col+3] == board[col+6]):
            draw_vertical_winning_line(col, player)
            return True

    # horizotal win
    for rows in range(BOARD_ROWS):
        if (rows == 0):
            if (board[rows] == board[rows+1] == board[rows+2]):
                draw_horizontal_winning_line(rows, player)
                return True
        if(rows == 1):
            if (board[rows+2] == board[rows+3] == board[rows+4]):
                draw_horizontal_winning_line(rows, player)
                return True
        if(rows == 2):
            if (board[rows+4] == board[rows+5] == board[rows+6]):
                draw_horizontal_winning_line(rows, player)
                return True

    # asc diagonal win check
    if (board[0] == board[4] == board[8]):
        draw_desc_diagonal(player)
        return True

    # desc diagonal win chek
    if (board[2] == board[4] == board[6]):
        draw_asc_diagonal(player)
        return True
    elif (int in board):
        return False
    return 'draw'

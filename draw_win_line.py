
import pygame
from constants import *
import screen

def draw_vertical_winning_line(row, player):
    """
    It draws a vertical line on the screen
    
    :param row: the row of the winning line
    :param player: the player who won
    """
    posX = row * SQUARE_SIZE + SQUARE_SIZE//2

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen.screen, color, (posX, 15),
                     (posX, HEIGHT - 15), LINE_WIDTH)


def draw_horizontal_winning_line(row, player):
    """
    It draws a horizontal line across the screen, at the height of the row that was passed in, and in
    the color of the player that won
    
    :param row: the row of the winning line
    :param player: the player who won
    """
    posY = row * SQUARE_SIZE + SQUARE_SIZE//2

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen.screen, color, (15, posY),
                     (WIDTH - 15, posY), WIN_LINE_WIDTH)


def draw_asc_diagonal(player):
    """
    It draws a diagonal line from the top left corner to the bottom right corner
    
    :param player: The player who won the game
    """
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen.screen, color, (15, HEIGHT - 15),
                     (WIDTH - 15, 15), WIN_LINE_WIDTH)


    """
    It draws a diagonal line from the top left corner to the bottom right corner of the screen
    
    :param player: the player who won
    """
def draw_desc_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen.screen, color, (15, 15),
                     (WIDTH - 15, HEIGHT - 15), WIN_LINE_WIDTH)

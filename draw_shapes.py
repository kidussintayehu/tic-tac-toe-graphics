
import pygame
import screen as sc
from constants import *


def draw_cicle(row, col):
    pygame.draw.circle(sc.screen,
                       CIRCLE_COLOR, (int(col * SQUARE_SIZE + SQUARE_SIZE//2),
                                      int(row * SQUARE_SIZE + SQUARE_SIZE//2)),
                       CIRCLE_RADIUS, CIRCLE_WIDTH)


def draw_x(row, col):
    pygame.draw.line(sc.screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE -
                                           SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
    pygame.draw.line(sc.screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                     (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)

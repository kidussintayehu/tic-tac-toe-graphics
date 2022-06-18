import pygame
import screen as sc
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15

SQUARE_SIZE = 200

BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)

CROSS_COLOR = (220, 0, 20)



    """
    It draws four lines, two horizontal and two vertical, to create a 3x3 grid
    """
def draw_lines():
    # 1 horizontal
    pygame.draw.line(sc.screen, LINE_COLOR, (0, SQUARE_SIZE),
                     (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    # 2 horizontal
    pygame.draw.line(sc.screen, LINE_COLOR, (0, 2 * SQUARE_SIZE),
                     (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)

    # 1 vertical
    pygame.draw.line(sc.screen, LINE_COLOR, (SQUARE_SIZE, 0),
                     (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    # 2 vertical
    pygame.draw.line(sc.screen, LINE_COLOR, (2 * SQUARE_SIZE, 0),
                     (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

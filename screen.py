# import pygame
# import sys
#
# import OpenGL


import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
WIDTH = 600
HEIGHT = 600
BG_COLOR = (28, 170, 156)
pygame.init()
display = (400, 300)
# screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# textfont=pygame.font.SysFont('monospace',30)
pygame.display.set_caption('TIC TAC TOE')

screen.fill(BG_COLOR)

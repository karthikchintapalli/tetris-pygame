import pygame
import random
import time

pygame.init()
from block import *
clock = pygame.time.Clock()
headfont = pygame.font.SysFont(None, 40)
scorefont = pygame.font.SysFont(None, 30)
screen = pygame.display.set_mode((screenwidth * ul, screenheight * ul))
pygame.display.set_caption('Tetris')
pygame.display.update()
from gameplay import *

game = Gameplay()
game.initGame()
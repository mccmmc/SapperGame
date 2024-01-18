import pygame

from end import win, wasted
from game_action import game
from menu import main_menu
from utils import SCREEN_SIZE

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)

clock = pygame.time.Clock()
running = True

while running:
    bombs = main_menu(screen)
    result = game(screen, bombs)
    if result:
        win(screen)
    else:
        wasted(screen)

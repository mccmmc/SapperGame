import pygame

from game_action import game
from menu import main_menu
from utils import terminate, SCREEN_SIZE, FPS

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)


def end_game(surface):
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
        surface.fill('red')
        pygame.display.update()
        clock.tick(FPS)


clock = pygame.time.Clock()
running = True

while running:
    main_menu(screen)
    game(screen)
    # end_game(screen)

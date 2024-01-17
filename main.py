import pygame

from menu import main_menu
from utils import terminate, SCREEN_SIZE, FPS

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)


def game(surface):
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
        screen.fill('red')
        pygame.display.update()
        clock.tick(FPS)


clock = pygame.time.Clock()
running = True

while running:
    main_menu(screen)
    game(screen)

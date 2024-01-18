import pygame

from utils import terminate, SCREEN_SIZE


def win(surface):
    background_img = pygame.transform.scale(pygame.image.load(r'./data/end.jpg'), SCREEN_SIZE)
    surface.blit(background_img, (0, 0))

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            if event.type == pygame.MOUSEBUTTONDOWN:
                return

        pygame.display.update()


def wasted(surface):
    background_img = pygame.transform.scale(pygame.image.load(r'./data/wasted.jpg'), SCREEN_SIZE)
    surface.blit(background_img, (0, 0))

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            if event.type == pygame.MOUSEBUTTONDOWN:
                return

        pygame.display.update()

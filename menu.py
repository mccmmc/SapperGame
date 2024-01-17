import pygame

from utils import terminate, FPS, SCREEN_SIZE


def main_menu(surface):
    intro_text = ["ЗАСТАВКА", "",
                  "Правила игры",
                  "Если в правилах несколько строк,",
                  "приходится выводить их построчно"]

    background_img = pygame.transform.scale(pygame.image.load(r'./data/background.jpg'), SCREEN_SIZE)
    font_obj = pygame.font.Font(None, 20)
    surface.blit(background_img, (0, 0))
    text_coord = 50

    for line in intro_text:
        string_rendered = font_obj.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        surface.blit(string_rendered, intro_rect)

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.update()
        clock.tick(FPS)

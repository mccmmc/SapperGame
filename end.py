import pygame

from utils import terminate, SCREEN_SIZE


def win(surface, score):
    background_img = pygame.transform.scale(pygame.image.load(r'./data/end.jpg'), SCREEN_SIZE)
    surface.blit(background_img, (0, 0))

    render_result(surface, score)

    running = True

    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                terminate()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return

        pygame.display.update()


def wasted(surface, score):
    background_img = pygame.transform.scale(pygame.image.load(r'./data/wasted.jpg'), SCREEN_SIZE)
    surface.blit(background_img, (0, 0))

    render_result(surface, score)

    running = True

    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                terminate()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return

        pygame.display.update()


def render_result(surface, score):
    intro_text = [f"вас счет: {score}",
                  "Отличный результат!",
                  "Нажмите пробел, чтобы попробовать еще раз"]

    font_obj = pygame.font.Font(None, 20)
    text_coord = 5

    for line in intro_text:
        string_rendered = font_obj.render(line, 1, pygame.Color('red'))
        intro_rect = string_rendered.get_rect()

        text_coord += 5
        intro_rect.top = text_coord

        intro_rect.x = 5
        text_coord += intro_rect.height
        surface.blit(string_rendered, intro_rect)

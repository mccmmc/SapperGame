import pygame

from utils import terminate, FPS, SCREEN_SIZE, load_image


class Easy(pygame.sprite.Sprite):
    image = load_image('easy.png')

    def __init__(self, *groups):
        super().__init__(*groups)
        self.rect = self.image.get_rect()

        self.rect.x = 91
        self.rect.y = 130

        self.max_bomb = 0

    def update(self, event):
        if event and event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(*event.pos):
            print('easy')
            self.max_bomb = 20


class Medium(pygame.sprite.Sprite):
    image = load_image('medium.png')

    def __init__(self, *groups):
        super().__init__(*groups)
        self.rect = self.image.get_rect()

        self.rect.x = 91
        self.rect.y = 184

        self.max_bomb = 0

    def update(self, event):
        if event and event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(*event.pos):
            print('medium')
            self.max_bomb = 40


class Hard(pygame.sprite.Sprite):
    image = load_image('hard.png')

    def __init__(self, *groups):
        super().__init__(*groups)
        self.rect = self.image.get_rect()

        self.rect.x = 91
        self.rect.y = 238

        self.max_bomb = 0

    def update(self, event):
        if event and event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(*event.pos):
            print('hard')
            self.max_bomb = 60


def main_menu(surface):
    intro_text = ["Это бетка, cделанная для защиты,",
                  "Я сильно не успеваю,",
                  "Итоговый код скину позже,",
                  "Извините :("]

    background_img = pygame.transform.scale(pygame.image.load(r'./data/menu.png'), SCREEN_SIZE)
    font_obj = pygame.font.Font(None, 20)
    surface.blit(background_img, (0, 0))
    text_coord = 5

    for line in intro_text:
        string_rendered = font_obj.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 5
        intro_rect.top = text_coord
        intro_rect.x = 5
        text_coord += intro_rect.height
        surface.blit(string_rendered, intro_rect)

    all_sprites = pygame.sprite.Group()

    easy = Easy(all_sprites)
    medium = Medium(all_sprites)
    hard = Hard(all_sprites)

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            all_sprites.update(event)

        for i in [easy, medium, hard]:
            if i.max_bomb != 0:
                return i.max_bomb

        all_sprites.draw(surface)
        pygame.display.update()
        clock.tick(FPS)

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
    result, score = game(screen, bombs)

    with open('best_result.txt', 'w', encoding='utf8') as file:

        print(f'Прошлый результат {score}! \n'
              f'Отлично! Класс! Супер круто! \n'
              f'Молодец! Так держать! \n'
              f'Умничка! Ты реально крут! \n', file=file)

    if result:
        win(screen, score)

    else:
        wasted(screen, score)

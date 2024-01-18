import random

import pygame

from utils import FPS, terminate


class Board:
    def __init__(self, screen, width, height):
        self.board = [[-1] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

        self.screen = screen
        self.width = width
        self.height = height

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                pygame.draw.rect(
                    surface=self.screen,
                    color='white',
                    rect=(
                        self.left + self.cell_size * x,
                        self.top + self.cell_size * y,
                        self.cell_size,
                        self.cell_size,
                    ),
                    width=1
                )

                # if self.board[y][x] == 10:  # bomb render
                #     self.screen.fill(color='blue',
                #                      rect=(
                #                          self.left + self.cell_size * x + 1,
                #                          self.top + self.cell_size * y + 1,
                #                          self.cell_size - 2,
                #                          self.cell_size - 2,
                #                      )
                #                      )

    def get_cell(self, mouse_pos):
        mx, my = mouse_pos
        cell_x = (mx - self.left) // self.cell_size
        cell_y = (my - self.left) // self.cell_size

        if 0 <= cell_y < self.height and 0 <= cell_x < self.width:
            return cell_x, cell_y

        return None

    def on_click(self, cell_coords):
        pos_x, pos_y = cell_coords

        self.change(pos_x, pos_y)

    def change(self, x, y):
        self.board[y][x] = int(not bool(self.board[y][x]))  # bin change

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)

        try:
            self.on_click(cell)
        except TypeError:
            return None


class Sapper(Board):
    def __init__(self, screen, width, height, max_bomb):
        super().__init__(screen, width, height)

        self.font = pygame.font.Font(None, 30)
        self.game_status = True
        self.game_final = False
        self.max_bomb = max_bomb

        self.reset_board()

    def reset_board(self):
        bomb_counter = 0

        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):

                bomb_near = self.check_cell(x, y)

                if bomb_near <= 4 and bomb_counter <= self.max_bomb:
                    choice = random.choice([-1, -1, -1, 10])
                    self.board[y][x] = choice

                    if choice == 10:
                        bomb_counter += 1

    def render(self):
        close_count = 0

        super().render()
        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                if 10 > self.board[y][x] >= 0:
                    self.screen.blit(self.font.render(str(self.board[y][x]), True, (255, 255, 255)),
                                     (self.left + self.cell_size * x + 1, self.top + self.cell_size * y + 1))
                if self.board[y][x] == -1:
                    close_count += 1

        if close_count == 0:
            self.game_status = False
            self.game_final = True

    def open_cell(self, mouse_pos):
        try:
            x, y = self.get_cell(mouse_pos)
            try:
                self.open_neighbor(x, y)
            except AssertionError:
                self.game_status = False
        except TypeError:
            print('error')

    def open_neighbor(self, x, y):
        number = self.check_cell(x, y)

        if self.board[y][x] != 0 and number == 0:
            self.board[y][x] = number

            if x - 1 >= 0:
                self.open_neighbor(x - 1, y)

            if y - 1 >= 0:
                self.open_neighbor(x, y - 1)

            if x + 1 < len(self.board[y]):
                self.open_neighbor(x + 1, y)

            if y + 1 < len(self.board[y]):
                self.open_neighbor(x, y + 1)

        self.board[y][x] = number
        return

    def check_cell(self, x, y):
        if self.board[y][x] == 10:
            raise AssertionError
        cells = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                try:
                    assert y + i >= 0 and x + j >= 0
                    if (i, j) == (0, 0):
                        continue
                    if self.board[y + i][x + j] == 10:
                        cells += 1
                except AssertionError:
                    continue
                except IndexError:
                    continue
        return cells


def game(surface, bomb):
    n = 12
    max_bomb = bomb

    sapper_game = Sapper(surface, n, n, max_bomb)
    sapper_game.set_view(50, 50, 250 // n)

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                sapper_game.open_cell(event.pos)

        if not sapper_game.game_status:
            return sapper_game.game_final

        surface.fill('black')
        sapper_game.render()
        pygame.display.update()
        clock.tick(FPS)

import pygame
import constant as SET_UP
import math

from main import FONT


class Tile:
    COLORS = [
        (237, 229, 218),
        (238, 225, 201),
        (243, 178, 122),
        (246, 150, 101),
        (247, 124, 95),
        (247, 95, 59),
        (237, 208, 115),
        (237, 204, 99),
        (236, 202, 80),
    ]

    def __init__(self, value, row, col):
        self.value = value
        self.row = row
        self.col = col
        self.x = col * SET_UP.RECT_WIDTH
        self.y = row * SET_UP.RECT_HEIGHT

    def get_color(self):
        """
        f(2) -> 0
        f(4) -> 1
        f(8) -> 2
        f(16) -> 3
        """
        color_index = int(math.log2(self.value) - 1)
        color = self.COLORS[color_index]
        return color

    def draw(self, window):
        color = self.get_color()
        pygame.draw.rect(
            window, color, (self.x, self.y, SET_UP.RECT_WIDTH, SET_UP.RECT_HEIGHT)
        )  # Rectagle used in the game

        # text in middle of rectangle
        text = FONT.render(str(self.value), 1, SET_UP.FONT_COLOR)

        window.blit(
            text,
            (
                self.x + (SET_UP.RECT_WIDTH / 2 - text.get_width() / 2),
                self.y + (SET_UP.RECT_HEIGHT / 2 - text.get_height() / 2),
            ),
        )

    def move(self, delta):
        pass

    def set_pos(self):
        pass

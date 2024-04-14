import pygame
import random
import math

# Constant import
import constant as SET_UP
from entities import Tiles

# init
pygame.init()


FONT = pygame.font.SysFont("comicsans", 60, bold=False)

# Game configurations
WINDOW = pygame.display.set_mode((SET_UP.WIDTH, SET_UP.HEIGHT))  # display configuration
pygame.display.set_caption("2048")  # Set title for game window


def draw_grid(window):
    """
    La función draw_grid(window) toma un parámetro llamado window, que representa la ventana de Pygame en la que se dibujará la cuadrícula.

    El bucle for row in range(1, SET_UP.ROW) itera a través de las filas de la cuadrícula.
    SET_UP.ROW es el número total de filas en la cuadrícula.

    Para cada fila, calcula la coordenada y en la que se dibujará la línea horizontal.

    Luego, utiliza pygame.draw.line() para dibujar una línea horizontal desde (0, y) hasta (SET_UP.WIDTH, y) con el color y grosor especificados en SET_UP.OUTLINE_COLOR y SET_UP.OUTLINE_THICKNESS.

    El segundo bucle for col in range(1, SET_UP.COLS) hace lo mismo para las columnas.

    Calcula la coordenada x para cada columna y dibuja una línea vertical desde (x, 0) hasta (x, SET_UP.HEIGHT).

    Finalmente, se dibuja un rectángulo en toda la ventana utilizando pygame.draw.rect().

    El rectángulo tiene las mismas dimensiones que la ventana (ancho y alto especificados en SET_UP.WIDTH y SET_UP.HEIGHT) y se dibuja con el color
    y grosor especificados en SET_UP.OUTLINE_COLOR y SET_UP.OUTLINE_THICKNESS.
    """
    for row in range(1, SET_UP.ROWS):
        y = row * SET_UP.RECT_HEIGHT
        pygame.draw.line(
            window,
            SET_UP.OUTLINE_COLOR,
            (0, y),
            (SET_UP.WIDTH, y),
            SET_UP.OUTLINE_THICKNESS,
        )

    for col in range(1, SET_UP.COLS):
        x = col * SET_UP.RECT_HEIGHT
        pygame.draw.line(
            window,
            SET_UP.OUTLINE_COLOR,
            (x, 0),
            (x, SET_UP.HEIGHT),
            SET_UP.OUTLINE_THICKNESS,
        )

    pygame.draw.rect(
        window,
        SET_UP.OUTLINE_COLOR,
        (0, 0, SET_UP.WIDTH, SET_UP.HEIGHT),
        SET_UP.OUTLINE_THICKNESS,
    )


def draw(window, tiles):
    window.fill(SET_UP.BACKGROUND_COLOR)

    for tile in tiles.values():
        tile.draw(window)

    draw_grid(window)

    pygame.display.update()


def get_random_pos(tiles):
    row = None
    col = None
    while True:
        row = random.randrange(0, SET_UP.ROWS)
        col = random.randrange(0, SET_UP.COLS)
        if f"{row}{col}" not in tiles:
            break

    return row, col


def move_tiles(window, tiles, clock, direction):
    updated = True
    blocks = set()

    if direction == "left":
        sort_func = lambda x: x.col
        reverse = False
        delta = (-SET_UP.MOVE_VEL, 0)
        boundary_check = lambda tile: tile.col == 0
        get_next_tile = lambda tile: tiles.get(f"{tile.row}{tile.col - 1}")
        merge_check = lambda tile, next_tile: tile.x > next_tile.x + SET_UP.MOVE_VEL
        move_check = (
            lambda tile, next_tile: tile.x
            > next_tile.x + SET_UP.RECT_WIDTH + SET_UP.MOVE_VEL
        )
        ceil = True
    elif direction == "right":
        sort_func = lambda x: x.col
        reverse = True
        delta = (SET_UP.MOVE_VEL, 0)
        boundary_check = lambda tile: tile.col == SET_UP.COLS - 1
        get_next_tile = lambda tile: tiles.get(f"{tile.row}{tile.col + 1}")
        merge_check = lambda tile, next_tile: tile.x < next_tile.x - SET_UP.MOVE_VEL
        move_check = (
            lambda tile, next_tile: tile.x + SET_UP.RECT_WIDTH + SET_UP.MOVE_VEL
            < next_tile.x
        )
        ceil = False
    elif direction == "up":
        sort_func = lambda x: x.row
        reverse = False
        delta = (0, -SET_UP.MOVE_VEL)
        boundary_check = lambda tile: tile.row == 0
        get_next_tile = lambda tile: tiles.get(f"{tile.row - 1}{tile.col}")
        merge_check = lambda tile, next_tile: tile.y > next_tile.y + SET_UP.MOVE_VEL
        move_check = (
            lambda tile, next_tile: tile.y
            > next_tile.y + SET_UP.RECT_HEIGHT + SET_UP.MOVE_VEL
        )
        ceil = True
    elif direction == "down":
        sort_func = lambda x: x.row
        reverse = True
        delta = (0, SET_UP.MOVE_VEL)
        boundary_check = lambda tile: tile.row == SET_UP.ROWS - 1
        get_next_tile = lambda tile: tiles.get(f"{tile.row + 1}{tile.col}")
        merge_check = lambda tile, next_tile: tile.y < next_tile.y - SET_UP.MOVE_VEL
        move_check = (
            lambda tile, next_tile: tile.y + SET_UP.RECT_HEIGHT + SET_UP.MOVE_VEL
            < next_tile.y
        )
        ceil = False

    while updated:
        clock.tick(SET_UP.FPS)
        updated = False
        sorted_tiles = sorted(tiles.values(), key=sort_func, reverse=reverse)

        for i, tile in enumerate(sorted_tiles):
            if boundary_check(tile):
                continue
            next_tile = get_next_tile(tile)
            if not next_tile:
                tile.move(delta)
            elif (
                tile.value == next_tile.value
                and tile not in blocks
                and next_tile not in blocks
            ):
                if merge_check(tile, next_tile):
                    tile.move(delta)
                else:
                    next_tile.value *= 2
                    sorted_tiles.pop(i)
                    blocks.add(next_tile)
            elif move_check(tile, next_tile):
                tile.move(delta)
            else:
                continue

            tile.set_pos(ceil)
            updated = True

        update_tiles(window, tiles, sorted_tiles)
    return end_move(tiles)


def end_move(tiles):
    if len(tiles) == 16:
        return "Lost"

    row, col = get_random_pos(tiles)
    tiles[f"{row}{col}"] = Tiles.Tile(random.choice([2, 4]), row, col)
    return "Continue"


def update_tiles(window, tiles, sorted_tiles):
    tiles.clear()
    for tile in sorted_tiles:
        tiles[f"{tile.row}{tile.col}"] = tile

    draw(window, tiles)


def generate_tiles():
    tiles = {}  # empty dictionary
    for _ in range(2):
        row, col = get_random_pos(tiles)
        tiles[f"{row}{col}"] = Tiles.Tile(2, row, col)

    return tiles


def main(window):
    clock = pygame.time.Clock()
    run = True

    tiles = generate_tiles()

    while run:
        clock.tick(SET_UP.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move_tiles(window, tiles, clock, "left")
                if event.key == pygame.K_RIGHT:
                    move_tiles(window, tiles, clock, "right")
                if event.key == pygame.K_UP:
                    move_tiles(window, tiles, clock, "up")
                if event.key == pygame.K_DOWN:
                    move_tiles(window, tiles, clock, "down")

        draw(window, tiles)

    pygame.quit()


if __name__ == "__main__":
    main(WINDOW)

import pygame
import random
import math

# Constant import
import Tiles.Tile as Tiles
import constant as SET_UP
# init
pygame.init()

"""
    Game font configuration
    init custom font
    name : Winter Pixel 24 BOLD
    from: https://www.fontspace.com/category/pixel
"""
# font_path = "/font/StWinterPixel24BoldDemoBold-BWRz5.otf"
# font_size = 24
# custom_font = pygame.font.Font(font_path, font_size)

FONT = pygame.font.SysFont("Roboto", 60, bold=False)

# Game configurations
WINDOW = pygame.display.set_mode((SET_UP.WIDTH, SET_UP.HEIGHT))  # display configuration
pygame.display.set_caption("2048")  # Set title for game window


def draw_grid(window):
    '''
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
    '''
    for row in range(1,SET_UP.ROW):
        y = row * SET_UP.RECT_HEIGHT
        pygame.draw.line(window, SET_UP.OUTLINE_COLOR,(0,y),(SET_UP.WIDTH,y),SET_UP.OUTLINE_THICKNESS)

    for col in range(1,SET_UP.COLS):
        x = col * SET_UP.RECT_HEIGHT
        pygame.draw.line(window, SET_UP.OUTLINE_COLOR,(x,0),(x,SET_UP.HEIGHT),SET_UP.OUTLINE_THICKNESS)

    pygame.draw.rect(window, SET_UP.OUTLINE_COLOR, (0, 0, SET_UP.WIDTH, SET_UP.HEIGHT),SET_UP.OUTLINE_THICKNESS)


def draw(window,tiles):
    window.fill(SET_UP.BACKGROUND_COLOR)

    for tile in tiles.values():
        tile.draw(window)
    
    draw_grid(window)

    pygame.display.update()


def main(window):
    clock = pygame.time.Clock()
    run = True
    
    tiles =  {}


    while run:
        clock.tick(SET_UP.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        draw(window,tiles)

    pygame.quit()


if __name__ == "__main__":
    main(WINDOW)

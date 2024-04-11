import pygame
import random
import math

# Constant import
import constant as SET_UP 

# init
pygame.init()

'''
    Game font configuration
    init custom font
    name : Winter Pixel 24 BOLD
    from: https://www.fontspace.com/category/pixel
'''
# font_path = "/font/StWinterPixel24BoldDemoBold-BWRz5.otf"
# font_size = 24
# custom_font = pygame.font.Font(font_path, font_size)

FONT = pygame.font.SysFont("Roboto",60,bold=False)

# Game configurations
WINDOW = pygame.display.set_mode((SET_UP.WIDTH,SET_UP.HEIGHT)) # display configuration
pygame.display.set_caption("2048") # Set title for game window


def main(window):
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(SET_UP.FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
    
    pygame.quit()

if __name__ =="__main__":
    main(WINDOW)
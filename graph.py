import pygame
import sprites

size = 12, 8
tile_size = 64
size_pix = width, height = size[0] * tile_size, size[1] * tile_size
screen = None

tiles = [[pygame.Rect(x * tile_size, y * tile_size, tile_size, tile_size) for y in range(size[1])] for x in range(size[0])]

def init():
    global screen
    screen = pygame.display.set_mode(size_pix, vsync=True)
    pygame.display.set_caption("Castle wars")
    pygame.display.set_icon(sprites.face)
    pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)


def clear():
    for col in tiles:
        for tile in col:
            screen.blit(sprites.grass, tile)

def flip():
    pygame.display.flip()            
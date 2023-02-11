import pygame

# GLOBAL VARS
MAP_RES = 30
MAP_SIZE = 20
GRID_LINE_WIDTH = 1
GRID_COLOR = (190, 190, 190)
SCREEN = pygame.display.set_mode((MAP_RES * MAP_SIZE, MAP_RES * MAP_SIZE))

# INIT
pygame.init()
pygame.display.set_caption("Path Finder")
